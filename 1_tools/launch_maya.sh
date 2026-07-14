#!/bin/zsh
# ============================================================
# launch_maya.sh
#
# Custom Maya launcher for macOS.
# Sets up pipeline environment variables (Python paths, plugin
# paths, shelves) before starting Maya.
#
# Usage:
#   ./launch_maya.sh                     # launch Maya, no scene
#   ./launch_maya.sh /path/to/scene.ma   # launch Maya and open a scene
# ============================================================


# --- PROJECT ROOT ---------------------------------------------------

export PROJECT_ROOT="$HOME/Documents/maya/projects/picre"

# --- PIPELINE / SOFTWARE PATHS --------------------------------------

export MAYA_VERSION="2027"

export SOFTWARE_PATH="/Applications/Autodesk/maya${MAYA_VERSION}/"


export PIPELINE_PATH="$PROJECT_ROOT/dev"

export PLUGINS_PATH="$SOFTWARE_PATH/plug-ins"


# --- PYTHON ----------------------------------------------------------
export PYTHONPATH="$PIPELINE_PATH:$PYTHONPATH"

# --- PLUGINS -----------------------------------------------------------
export MAYA_PLUG_IN_PATH="$PLUGINS_PATH:$MAYA_PLUG_IN_PATH"

# --- SHELVES -----------------------------------------------------------
export MAYA_SHELF_PATH="$SOFTWARE_PATH/shelf:$MAYA_SHELF_PATH"

# --- DISABLE AUTODESK DIAGNOSTIC/ERROR REPORTING ------------------------
export MAYA_DISABLE_CIP=1
export MAYA_DISABLE_CER=1


# --- LOCATE THE MAYA EXECUTABLE --------------------------------------------
MAYA_APP="/Applications/Autodesk/maya${MAYA_VERSION}/Maya.app/Contents/MacOS/Maya"

if [[ ! -x "$MAYA_APP" ]]; then
  echo "Maya executable not found at: $MAYA_APP"
  echo "Check MAYA_VERSION or your Autodesk install path."
  exit 1
fi

# --- LAUNCH ------------------------------------------------------------
if [[ -z "$1" ]]; then
  "$MAYA_APP" &
else
  "$MAYA_APP" -file "$1" &
fi
disown

exit 
