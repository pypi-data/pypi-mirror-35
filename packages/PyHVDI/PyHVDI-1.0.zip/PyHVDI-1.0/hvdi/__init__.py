"""\
  HawkVoice Direct Interface (HVDI) cross platform network voice library
  Copyright (C) 2001-2004 Phil Frisbie, Jr. (phil@hawksoft.com)

  This is Python ctypes bindings for HawkVoiceDI
  Copyright (C) 2018 by Dalen Bernaca
                        dbernaca@gmail.com

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Library General Public
  License as published by the Free Software Foundation; either
  version 2 of the License, or (at your option) any later version.
  
  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Library General Public License for more details.
    
  You should have received a copy of the GNU Library General Public
  License along with this library; if not, write to the
  Free Software Foundation, Inc., 59 Temple Place - Suite 330,
  Boston, MA  02111-1307, USA.
      
  Or go to http://www.gnu.org/copyleft/lgpl.html

  The disclaimer above applies both to the HawkVoiceDI C part and the Python bindings as well.
"""

MAJOR_VERSION  = 0
MINOR_VERSION  = 91
VERSION_STRING = 'HVDI 0.91 beta'

from constants import *
from structures import *
from lib import *
import crypt
import hvdi

# We do not want following modules,
# that were automatically imported, in our namespace.
# It ruins the design.
try: del tweaks
except: pass
try: del help_support
except: pass