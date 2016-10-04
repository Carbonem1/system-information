System Information

A python script used to grab system information.

Uses:
./system_information.py (dump system information to the console)
./system_information.py -f (dump system information to system_information_logs/system_information.log)

Example output (values omitted):
---------- Timestamp ----------
2016-01-01 11:11:00
---------- Kernel Output ----------
Linux example-system x.x.x.x.default x86_64 x86_64 x86_64 GNU/Linux
---------- Facter Output ----------
architecture =>
bios_release_date =>
bios_vendor =>
bios_version =>
blockdevice_sda_model =>
blockdevice_sda_size =>
blockdevice_sda_vendor =>
blockdevice_sdb_model =>
blockdevice_sdb_size =>
blockdevice_sdb_vendor =>
blockdevice_sdc_model =>
blockdevice_sdc_size =>
blockdevice_sdc_vendor =>
blockdevice_sdd_model =>
blockdevice_sdd_size =>
blockdevice_sdd_vendor =>
blockdevice_sde_model =>
blockdevice_sde_size =>
blockdevice_sde_vendor =>
blockdevice_sdf_model =>
blockdevice_sdf_size =>
blockdevice_sdf_vendor =>
blockdevice_sdg_model =>
blockdevice_sdg_size =>
blockdevice_sdg_vendor =>
blockdevice_sdh_model =>
blockdevice_sdh_size =>
blockdevice_sdh_vendor =>
blockdevice_sdi_model =>
blockdevice_sdi_size =>
blockdevice_sdi_vendor =>
blockdevice_sdj_model =>
blockdevice_sdj_size =>
blockdevice_sdj_vendor =>
blockdevice_sdk_model =>
blockdevice_sdk_size =>
blockdevice_sdk_vendor =>
blockdevice_sdl_model =>
blockdevice_sdl_size =>
blockdevice_sdl_vendor =>
blockdevice_sdm_model =>
blockdevice_sdm_size =>
blockdevice_sdm_vendor =>
blockdevice_sdn_model =>
blockdevice_sdn_size =>
blockdevice_sdn_vendor =>
blockdevice_sdo_model =>
blockdevice_sdo_size =>
blockdevice_sdo_vendor =>
blockdevice_sr0_model =>
blockdevice_sr0_size =>
blockdevice_sr0_vendor =>
blockdevices =>
boardmanufacturer =>
boardproductname =>
boardserialnumber =>
domain =>
facterversion =>
filesystems =>
fqdn =>
hardwareisa =>
hardwaremodel =>
hba0_device =>
hba0_driver =>
hba0_vendor =>
hostname =>
id =>
interfaces =>
ipaddress =>
ipaddress_eth4 =>
ipaddress_lo =>
is_pe =>
is_virtual =>
kernel =>
kernelmajversion =>
kernelrelease =>
kernelversion =>
lsbdistcodename =>
lsbdistdescription =>
lsbdistid =>
lsbdistrelease =>
lsbmajdistrelease =>
lsbrelease =>
macaddress =>
macaddress_eth4 =>
macaddress_eth5 =>
manufacturer =>
memoryfree =>
memoryfree_mb =>
memorysize =>
memorysize_mb =>
memorytotal =>
mtu_eth4 =>
mtu_eth5 =>
mtu_lo =>
netmask =>
netmask_eth4 =>
netmask_lo =>
network_eth4 =>
network_lo =>
operatingsystem =>
operatingsystemrelease =>
osfamily =>
path =>
physicalprocessorcount =>
processor0 =>
processor1 =>
processor2 =>
processor3 =>
processor4 =>
processor5 =>
processor6 =>
processor7 =>
processorcount =>
productname =>
ps =>
puppet_vardir =>
puppetversion =>
root_home =>
rubysitedir =>
rubyversion =>
selinux =>
serialnumber =>
sshdsakey =>
sshecdsakey =>
sshfp_dsa =>
sshfp_ecdsa =>
sshfp_rsa =>
sshrsakey =>
swapfree =>
swapfree_mb =>
swapsize =>
swapsize_mb =>
timezone =>
type =>
uniqueid =>
uptime =>
uptime_days =>
uptime_hours =>
uptime_seconds =>
uuid =>
virtual =>
---------- LSIUtil Output ----------

LSI Logic MPT Configuration Utility, Version 1.71, Sep 18, 2013

2 MPT Ports found

     Port Name         Chip Vendor/Type/Rev    MPT Rev  Firmware Rev  IOC
 1.  /example/port     Example                 000      000000000     0

Current active firmware version is 0000000 (xx.xx.xx.xx)
---------- Version Output ----------
xx.xx.xx.xx
---------- Devices Output ----------
Example SCSI storage controller: xxxx
Example Serial Attached SCSI controller: xxxx
