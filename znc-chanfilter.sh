#!/bin/bash

# check if the upstream checkout is a different hash than we have
# and if so, update the spec, submit SRPM to copr.

UPSTREAM_GIT="../znc-chanfilter/.git"

# committer
COMMITTER="RJ Bergeron <rbergero@gmail.com>"

# rpm bits
SPECDIR=$(rpm --eval '%{_specdir}')
SOURCEDIR=$(rpm --eval '%{_sourcedir}')

OUR_HASH=$(awk '$1 == "%global" && $2 == "hash" { print $3 }' znc-chanfilter.spec)
THEIR_HASH=$(git --git-dir="${UPSTREAM_GIT}" rev-parse HEAD)

if [ "${OUR_HASH}" != "${THEIR_HASH}" ] ; then

# create dirs for RPM
mkdir -p "${SPECDIR}" "${SOURCEDIR}"

logdate=$(date '+%a %b %e %Y')
shorthash=$(echo ${THEIR_HASH:0:7})

# use (g)sed to mangle specfile
sed -i -e "0,/${OUR_HASH}/s//${THEIR_HASH}/1" znc-chanfilter.spec
sed -i -e "s/%changelog/%changelog\\
* ${logdate} ${COMMITTER}\\
- update to ${THEIR_HASH}\\
/" znc-push.spec

cp znc-chanfilter.spec "${SPECDIR}"

# create tarball of upstream git
git --git-dir="${UPSTREAM_GIT}" archive --prefix="znc-chanfilter-${THEIR_HASH}/" --output="${SOURCEDIR}/znc-chanfilter-${shorthash}.tar.gz" HEAD

# pack it
#rpmbuild -bs "${SPECDIR}"/znc-chanfilter.spec

# submit for build
# copr-cli build znc-modules ~/rpmbuild/SRPMS/znc-chanfilter*.src.rpm
fi
