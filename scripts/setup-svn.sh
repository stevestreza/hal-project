#! /bin/bash

PROFILE="$HOME/.subversion/config"

echo $PROFILE;

touch $PROFILE;

echo "[miscellany]" >> $PROFILE;
echo "### Set global-ignores to a set of whitespace-delimited globs" >> $PROFILE;
echo "### which Subversion will ignore in its 'status' output, and" >> $PROFILE;
echo "### while importing or adding files and directories." >> $PROFILE;
echo "global-ignores = build *.pyc *.o *.lo *.la #*# .*.rej *.rej .*~ *~ .#* .DS_Store *~.nib *.tmp svn-*.tmp" >> $PROFILE;

#curl -O http://voxel.dl.sourceforge.net/sourceforge/pyserial/pyserial-2.4.tar.gz
