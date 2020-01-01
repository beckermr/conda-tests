echo "#!/bin/bash
echo \"!!!!!! PKG f !!!!!!\"
" > ${PREFIX}/bin/pkg-f
chmod u+x ${PREFIX}/bin/pkg-f

mkdir -p ${PREFIX}/lib
pushd ${PREFIX}/lib
ln -s test_f_file test_f_link
popd
