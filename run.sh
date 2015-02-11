cd jboss/jboss-jq/jboss-master/bin
chmod 777 *
./runmaster.sh &


sleep 30


cd ..
cd ..
cd jboss-cm/bin
chmod 777 *
./runcm.sh &
sleep 30


cd ..
cd ..
cd jboss-pm/bin 
chmod 777 *
./runpm.sh &



sleep 30
cd ..
cd ..
cd ..
cd ..
cd PC/PC
chmod 777 *
./runpc.sh &

