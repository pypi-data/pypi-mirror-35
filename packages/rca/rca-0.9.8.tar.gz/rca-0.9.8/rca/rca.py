#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Recompress Audio: a configuration-driven audio recompression utility
Copyright (C) 2018 Kevin R Croft

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__name__ = "rca"
__version__ = "0.9.8"
__author__ = "Kevin R Croft"

# Check if we're running Python 3.5+
import sys
if (sys.version_info) < (3, 5):
    print("CRITICAL: this script requires at least Python 3.5")
    sys.exit(1)

# Built-in modules
import os
import hashlib
import logging
import subprocess
from shutil import copy2, which
from fnmatch import fnmatch
from multiprocessing.dummy import Pool as ThreadPool

# Third-party module: appdirs, determines where RCA's config files
# should go on OSX, Windows, and Linux
try:
  from appdirs import user_data_dir
  _default_config_dir=user_data_dir(__name__, __author__)

except ImportError:
  print('CRITICAL: this script requires the appdirs module, '
        'install it with "sudo pip3 install appdirs"')
  sys.exit(1)

# Third-party module: yaml (yet another markup language) for
# user and application configurtion and record-storing files
try:
  import yaml
except ImportError:
  print('CRITICAL: this script requires the yaml module, '
        'install it with "sudo pip3 install yaml"')
  sys.exit(1)

# Third-party module: yaml (yet another markup language) for
# user and application configurtion and record-storing files
try:
  from colorlog import ColoredFormatter
except ImportError:
  print('CRITICAL: this script requires the colorlog module, '
        'install it with "sudo pip3 install colorlog"')
  sys.exit(1)


# Pull in our Track class (relative path)
from .track import Track

# Setup the logger
module = sys.modules['__main__'].__file__
formatter = ColoredFormatter("  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s")
stream = logging.StreamHandler()
stream.setFormatter(formatter)
log = logging.getLogger(module)
log.addHandler(stream)

def parse():
  import argparse

  parser = argparse.ArgumentParser(
    description='Conditionally (re)encode tracks using the specified codec')

  parser.add_argument("--version", action="version",
                      version="{} {}".format(__name__, __version__))

  parser.add_argument("-v", "--verbose", dest="verbose_count",
                      action="count", default=1,
                      help="increases log verbosity for each occurence.")

  initialize_config_dir(_default_config_dir)
  codecs=get_codecs(_default_config_dir)

  parser.add_argument(
    'codec',
    nargs='+',
    metavar='CODEC',
    choices=codecs,
    help='One or more encoding output formats: ' + ', '.join(codecs) +
         ". See the config_dir below that contains each codec's set of "
         'encoding profiles. Customize them or add your own!')

  parser.add_argument(
    '-f', '--force',
    action='store_true',
    default=False,
    help='Re-encode, even if RCA would normally not.')

  parser.add_argument(
    '-r', '--recurse',
    action='store_true',
    default=False,
    help='Run RCA in all subdirectories that contain properties.yml.')

  default_track_type='wav'
  parser.add_argument(
    '-t', '--track_type',
    default=default_track_type,
    help='Use a different source track type (ie: flac). The '
         'encoding application needs to be able to handle the '
         'input track type. '
         'Default is ' + default_track_type)

  default_output_dir=False
  parser.add_argument(
    '-o', '--output_dir',
    default=default_output_dir,
    help='Write encoded files to a different output directory. '
         'Default is ../current_directory-CODEC')

  parser.add_argument(
    '-d', '--config_dir',
    default=_default_config_dir,
    help='Use a different config directory. '
         'Default is ' + _default_config_dir)

  return parser.parse_args()


def get_codecs(config_dir):
  codecs = []
  if os.path.isdir(config_dir):
    for name in os.listdir(config_dir):
      codec_path = os.path.join(config_dir, name)
      if os.path.isfile(codec_path) and fnmatch(name, '*-profiles.yml'):
        codecs.append(name.replace('-profiles.yml', ''))
        log.debug('found codec profiles: ' + codec_path)

  if codecs:
    codecs.sort()
    codecs.append('all')

  return codecs


def initialize_config_dir(config_dir):
  os.makedirs(config_dir, exist_ok=True)
  script_path, script_name = os.path.split(os.path.realpath(__file__))
  source_dir = os.path.join(script_path, 'config')
  if os.path.isdir(source_dir):
    for source in os.listdir(source_dir):
      source_path = os.path.join(source_dir, source)
      if os.path.isfile(source_path) and fnmatch(source, '*.yml'):
        target_path = os.path.join(config_dir, source)
        if not os.path.exists(target_path):
          log.info('writing initial config: ' + target_path)
          copy2(source_path, target_path)
        else:
          log.info('using existing config: ' + target_path)

        target_dist_path = target_path + '.dist'
        if (not os.path.exists(target_dist_path) or
           os.path.getmtime(source_path) > os.path.getmtime(target_dist_path)):
          log.info('writing new distribution config: ' + target_dist_path)
          copy2(source_path, target_dist_path)
        else:
          log.info('found existing distribution config: ' + target_dist_path)
  else:
    log.error('missing source config path: ' + source_dir)

def get_tracks(track_type, defaults):
  tracks = dict()
  for f in os.listdir('.'):
    if os.path.isfile(f) and fnmatch(f, '*.' + track_type):
      t = Track(f, defaults.copy() )

      while t.n in tracks:
        t.n += 1
      tracks[t.n] = t

      log.debug('found track no.{} named "{}"'.format(t.n, t.basename))
  return tracks

def in_range(_range):
  matches=[]
  pprev=False
  prev=False

  for i in _range:
    if isinstance(i, int):
      i = int(i)
      matches.append(i)

      # scenarios: [1, -, 4, -, 6]
      if isinstance(pprev, int) and prev == '-':
        matches.extend(range(pprev + 1, i))

    pprev = prev
    prev = i

  return matches

def poulate_tier2(info, mprop):
  for key in info:
    if key in mprop['tier2']:
      for property, values in mprop['values'].items():
        if key in values:
          info[key][property] = key
          break

def poulate_track_properties(tracks, mprop):
  filename = 'properties.yml'
  if os.path.isfile(filename):
    with open(filename) as info_file:
      info = yaml.load(info_file)

      poulate_tier2(info, mprop)

      for key in info:
        if key in mprop['tier1']:
          [tracks[t].apply_properties(info[key]) for t in tracks]
          log.debug('applying {} properties to all tracks'.format(key) )
          break

      for key in info:
        if key in mprop['tier2']:
          selected = tracks
          if 'range' in info[key]:
            selected = in_range(info[key].pop('range'))
          log.debug('applying {} properties to {} tracks'.format(key, len(selected)))
          [tracks[t].apply_properties(info[key]) for t in selected]

      for key in info:
        if key not in mprop['tier1'] and key not in mprop['tier2']:
          for t in tracks:
            if key == tracks[t].basename:
              log.debug('applying {} properties individually'.format(key))
              tracks[t].apply_properties(info[key])

  else:
    log.warn('track information file {} not found in current '
             'directory'.format(filename))

# Return the md5 sum for a file
def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
      for chunk in iter(lambda: f.read(4096), b""):
        hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Return the application's checksum
def get_app_checksum(app):

    # absent until determined
    checksum=None

    # Only proceed if we can find the application in our PATH
    app_path = which(app)
    if os.path.isfile(app_path):
      checksum = md5(app_path)

    return checksum

# Determine and populate the tracks with the specified codec options
# given the track properties

def populate_track_desired_encoding(tracks, mprop, config_dir, codec):
  codec_app=None
  inout_args=None

  filename = os.path.join(config_dir, '{}-profiles.yml'.format(codec))

  if os.path.isfile(filename):
    with open(filename) as codec_file:
      codec = yaml.load(codec_file)
      codec_app = codec['application']
      codec_sum = get_app_checksum(codec_app)
      inout_args = codec['inout_args']
      log.info('loaded codec profiles from: ' + filename)
      log.debug('calculated {} checksum: {}'.format(codec_app, codec_sum))

      for t in tracks:
        track = tracks[t]
        track_properties = track.properties_as_str(mprop['order'])
        if track_properties in codec['combinations']:
          track.desired_options = codec['combinations'][track_properties]

          log.debug('setting desired encode options for {} '
                    'to: {}'.format(track.basename, track.desired_options))

        else:
          log.critical('no profile exists for properties "{}" in codec '
                       'file "{}"'.format(track_properties, filename))
  else:
    log.warn('codec file {} not found. Available codecs are: '
             '{}'.format(filename, ', '.join(get_codecs(config_dir))) )

  return codec_app, codec_sum, inout_args

# Populate the current encoding options from encoding.yml

def populate_track_actual_encoding(tracks, output_dir, codec):
  encoding_app=None
  encoding_sum=None

  filename = os.path.join(output_dir, '{}-encoding.yml'.format(codec) )
  if os.path.isfile(filename):
    with open(filename) as encoding_file:
      encoding = yaml.load(encoding_file)
      encoding_app = None if "application" not in encoding else encoding['application']
      encoding_sum = None if "checksum" not in encoding else  encoding['checksum']

      log.debug('loaded existing encoding settings from: ' + filename)
      log.debug('tracks were previously encoded with {} having checksum: '
               '{}'.format(encoding_app, encoding_sum))

      for n in tracks:
        name = tracks[n].basename
        if name in encoding:
          tracks[n].actual_options = encoding[name]
          log.debug('setting track {} actual encode options '
                    'to: {}'.format(n, encoding[name]))

  return encoding_app, encoding_sum

def save_encoding(tracks, output_dir, codec, desired_app, desired_sum, results):
  output = {}
  output['application'] = desired_app
  output['checksum'] = desired_sum
  recoded_list = [t for t, succeeded, message in results]

  for t in tracks:
    if t not in recoded_list:
      output[tracks[t].basename] = tracks[t].actual_options

  for t, succeeded, message in results:
    if succeeded:
      output[tracks[t].basename] = tracks[t].desired_options
    else:
      output[tracks[t].basename] = 'failed'
      log.warn('failed encoding track "{}" due to {}'.format(tracks[t].basename, message))

  filename = os.path.join(output_dir, '{}-encoding.yml'.format(codec) )
  with open(filename, 'w') as encoding_file:
    yaml.dump(output, encoding_file, default_flow_style=False)
    log.debug('saved encoding settings to: ' + filename)


# Define a callable to do the work. It should take one work item.
def encoder(cmd_args):

  # the first item is the track number, which we pop-off and return with
  # the result

  track_number = cmd_args.pop(0)

  # run it
  try:
    log.debug('launching "{}"'.format(' '.join(cmd_args)))
    completed = subprocess.run(' '.join(cmd_args),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

  except subprocess.CalledProcessError as err:
    log.error(err)

  else:
    if completed.returncode != 0:
      log.debug('return code for track '
                '{}: {}'.format(track_number, completed.returncode))

    if completed.stdout:
      log.debug('output for track {}: '
                '{}'.format(track_number, completed.stdout))

    if completed.stderr:
      log.debug('stderr for track {}: '
                '{}'.format(track_number, completed.stderr))

  return (track_number, completed.returncode == 0, completed.stderr)

def recode(tracks, selected, output_dir, codec, desired_app, inout_args):
  queue = []
  results = []

  for t in selected:
    encode_args = [t, desired_app]
    encode_args.extend(tracks[t].desired_options.split())

    outfile=os.path.join(output_dir, tracks[t].basename)
    inout_str = inout_args.format(infile=tracks[t].filename, outfile=outfile)

    encode_args.extend(inout_str.split())
    queue.append(encode_args)

  with ThreadPool(os.cpu_count()) as pool:
    results = pool.map(encoder, queue)

  return results

def run_dirs(recurse):
  cwd=os.getcwd()
  dirs=[]
  if recurse:
    for dirpath, name, filenames in os.walk('.'):
      if 'properties.yml' in filenames:
        dirs.append(os.path.join(cwd, dirpath))
  else:
    dirs.append(cwd)

  return dirs

# Get the filename from a cue line
def basename_from_cue(line):
  basename = None
  words = line.strip().split()
  if len(words) == 3 and words[0].lower() == 'file':
    basename = os.path.splitext( words[1].replace('"', '') )[0]
  return basename

# If a cue file exists, generate an equivalent based on our new compressed audio
def convert_cue(tracks, output_dir, codec):
  source_cue = None

  # do we have a local cue file?
  with os.scandir('.') as dir:
    for entry in dir:
      if entry.is_file() and entry.name.endswith('.cue'):
        source_cue = entry.name
        break

  # if yes ..
  if source_cue:
    # get a list of all our track base filenames (minus their extensions)
    track_names = [tracks[track].basename for track in tracks]

    # open our target cuefile
    target_cue = os.path.join(output_dir, source_cue)
    with open(target_cue,'w') as target:

      # open our source cuefile and walk line-by-line
      with open(source_cue) as source:
        for line in source:

          # print("cue line = ", line)
          # does the cue line have a filename?
          basename = basename_from_cue(line)

          # print("basename = ", basename)
          # if yes and it matches an exist track basename, write a new line
          if basename and basename in track_names:
            track_names.remove(basename)
            target.write('FILE "{}.{}" {}\n'.format(basename, codec.lower(), codec.upper()) )

          # otherwise just write the line as-is
          else:
            target.write(line)


def load_master_properties(config_dir):
  mprop = None
  filename = os.path.join(config_dir, 'master_properties.yml')
  if os.path.isfile(filename):
    with open(filename) as info_file:
      mprop = yaml.load(info_file)
  else:
    log.critical('cannot find master properties file "{}"'.format(filename))
  return mprop

def main():
  rcode = 1


  args = parse()

  # Set log level to WARN going more verbose for each new -v.
  log.setLevel(max(3 - args.verbose_count, 0) * 10)
  # logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
  log.info("Executing Recompress Audio (RCA) version %s" % __version__)

  # populate the users configuration directory if needed
  if args.config_dir != _default_config_dir:
    initialize_config_dir(args.config_dir)

  # load our master properties
  mprop = load_master_properties(args.config_dir)
  if mprop and 'defaults' in mprop:

    # populate the codecs specified by the user
    codecs = args.codec
    if 'all' in codecs:
      codecs = get_codecs(args.config_dir)
      codecs.remove('all')

    # Walk each working directory, if recursing
    for workdir in run_dirs(args.recurse):
      os.chdir(workdir)

      # Fetch the current track filenames
      tracks = get_tracks(args.track_type, mprop['defaults'])

      if tracks:
        # populate each track with its property info
        poulate_track_properties(tracks, mprop)

        for codec in codecs:
          # populate track with desired encoding options
          desired_app, desired_sum, inout_args = populate_track_desired_encoding(
                                        tracks, mprop, args.config_dir, codec)

          # make our output directory if needed
          output_dir=args.output_dir
          if not output_dir:
            output_dir=os.path.relpath('{}-{}'.format(os.getcwd(), codec))
          os.makedirs(output_dir, exist_ok=True)

          # populate track with actual encoding options, if the files have already been encoded
          actual_app, actual_sum = populate_track_actual_encoding(tracks,
                                                                  output_dir,
                                                                  codec)

          # if a cue file exists, covert it
          convert_cue(tracks, output_dir, codec)

          # determine which tracks need re-encoding
          selected = [t for t in tracks]
          if not args.force and actual_app == desired_app and actual_sum == desired_sum:
            selected = [t for t in tracks
                          if tracks[t].actual_options != tracks[t].desired_options]

          # if we need to encode one or more tracks ...
          if selected:
            try:
              results = recode(tracks, selected, output_dir, codec, desired_app, inout_args)
              log.debug(results)
              save_encoding(tracks, output_dir, codec, desired_app, desired_sum, results)
            except KeyboardInterrupt:
              log.critical('Program interrupted!')
          else:
            log.info('all tracks encoded with desired encoder and settings')

        # end-for codecs

      else: # tracks
        log.warn('no *.{} file found in the currect directory, skipping'.format(args.track_type))

    # end-for run_dirs

  else: # mprop
    log.warn('no master properties loaded; try reinstalling: '
           'pip3 install --upgrade --force-reinstall rca')

  # Stop logging
  logging.shutdown()
