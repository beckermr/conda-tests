echo "#!/bin/bash
echo \"!!!!!! PKG g !!!!!!\"
" > ${PREFIX}/bin/pkg-g
chmod u+x ${PREFIX}/bin/pkg-g

mkdir -p ${PREFIX}/lib
pushd ${PREFIX}/lib
echo "!!!!!! PKG g !!!!!!" > test_g_file
ln -s test_g_file test_g_link
popd
