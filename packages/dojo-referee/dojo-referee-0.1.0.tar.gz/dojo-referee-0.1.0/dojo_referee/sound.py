# Copyright (C) 2018 Caio Carrara <eu@caiocarrara.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# LICENSE for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import logging
import subprocess

from dojo_referee import settings


logger = logging.getLogger('dojo_referee')


def play(audio_file_path):
    try:
        sound_playing = subprocess.Popen(
            [settings.SOUND_EXEC, audio_file_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )
        return sound_playing
    except OSError as exc:
        msg = 'The following error happened trying to play finish sound'
        logger.error(msg, exc)


def play_begin():
    return play(settings.SOUND_BEGIN_FILE)


def play_finish():
    return play(settings.SOUND_FINISH_FILE)
