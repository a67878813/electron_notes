Install required dependencies and toolchain

sudo apt install git bc bison flex libssl-dev make libc6-dev libncurses5-dev


Install the 64-bit toolchain for a 64-bit kernel
sudo apt install crossbuild-essential-arm64

Get the kernel sources
To download the minimal source tree for the current branch, run:

git config --global http.proxy "http://192.168.88.235:3334"
git config --global https.proxy "sock5h://192.168.88.235:3333"
git clone --depth=1 https://github.com/raspberrypi/linux

git clone --depth=1 --branch <branch> https://github.com/raspberrypi/linux






### Kernel configuration

#### Apply the default configuration
For Raspberry Pi 5 default 64-bit build configuration:


cd linux
KERNEL=kernel_2712
make bcm2712_defconfig
失败，原因未知

The menuconfig utility has simple keyboard navigation. After a brief compilation, you’ll be presented with a list of submenus containing all the options you can configure. There are many options, so take your time to read through them and get acquainted.

Use the arrow keys to navigate, the Enter key to enter a submenu (indicated by --->), Escape twice to go up a level or exit, and the space bar to cycle the state of an option. Some options have multiple choices, in which case they’ll appear as a submenu and the Enter key will select an option. You can press h on most entries to get help about that specific option or menu.

### Saving your changes
Once you’re done making the changes you want, press Escape until you’re prompted to save your new configuration. By default, this will save to the .config file. You can save and load configurations by copying this file.

### Patching the kernel

### Version identification

 head Makefile -n 5

will show you the version the sources relate to:

VERSION = 6
PATCHLEVEL = 1
SUBLEVEL = 38


In this instance, the sources are for a 6.1.38 kernel. You can see what version you’re running on your system with the uname -r command.

### Applying patches

How you apply patches depends on the format in which the patches are made available. Most patches are a single file, and are applied with the **patch** utility. To download and patch our example kernel version with the real-time kernel patches:

wget https://www.kernel.org/pub/linux/kernel/projects/rt/6.1/patch-6.1.38-rt13-rc1.patch.gz
 gunzip patch-6.1.38-rt13-rc1.patch.gz
 cat patch-6.1.38-rt13-rc1.patch | patch -p1

 In our example we simply download the file, uncompress it, and then pass it to the **patch** utility using the **cat** tool and a Unix pipe.

Some patchsets come as mailbox-format patchsets, arranged as a folder of patch files. We can use Git to apply these patches to our kernel, but first we must configure Git to let it know who we are when we make these changes:
 git config --global user.name "Your name"
 git config --global user.email "your email in here"

 Once we’ve done this we can apply the patches:
  git am -3 /path/to/patches/*


### Customising the kernel version using LOCALVERSION
In addition to your kernel configuration changes, you may wish to adjust *LOCALVERSION* to ensure your new kernel does not receive the same version string as the upstream kernel. This clarifies that you are running your own kernel in the output of uname, and ensures that existing modules in /lib/modules are **not overwritten**.

To adjust LOCALVERSION, change the following line in .config:

**CONFIG_LOCALVERSION="-v7l-MY_CUSTOM_KERNEL"**



## Building the kernel

make -j4 Image.gz modules dtbs
sudo make modules_install
sudo cp arch/arm64/boot/dts/broadcom/*.dtb /boot/firmware/
sudo cp arch/arm64/boot/dts/overlays/*.dtb* /boot/firmware/overlays/
sudo cp arch/arm64/boot/dts/overlays/README /boot/firmware/overlays/
sudo cp arch/arm64/boot/Image.gz /boot/firmware/$KERNEL.img



### Kernel headers
If you are compiling a kernel **module** or similar, you will need the **Linux kernel headers**. These provide the various function and structure definitions required when compiling code that interfaces with the kernel.

If you have cloned the *entire kernel* from GitHub, the headers are *already* included in the source tree. If you don’t need all the extra files, it is possible to install only the kernel headers from the Raspberry Pi OS repo.

if you are using the 64-bit version of Raspberry Pi OS, run:

 sudo apt install linux-headers-rpi-v8

*It can take quite a while for this command to complete, as it installs a lot of small files. There is no progress indicator*

When a new kernel release is made, you will need the *headers that match that kernel version*. It can take several weeks for the repo to be updated to reflect the latest kernel version. If this happens, the best approach is to *clone the kernel*.


### **cross** build sources
64bit configs


For Raspberry Pi 5:


cd linux
KERNEL=kernel_2712
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- bcm2712_defconfig


*NOTE*
The standard, *bcm2711_defconfig*-based kernel (kernel8.img) also runs on Raspberry Pi 5. For **best** performance you should use **kernel_2712.img**, but for situations where a *4KB page size* is required then kernel8.img (kernel=kernel8.img) should be used.



#### Build with configs
NOTE
To speed up compilation on multiprocessor systems, and get some improvement on single-processor devices, use -j n, where n is the number of processors × 1.5. You can use the nproc command to see how many processors you have.
*For all 32-bit builds*

make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- zImage modules dtbs

*For all 64-bit builds*

NOTE
Note the difference between Image target between 32- and 64-bit.
__make -j 8 ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- Image modules dtbs__

#### Install directly onto the SD card


Having built the kernel, you need to *copy it onto your Raspberry Pi and install the modules*. This is best done directly using an SD card reader.


First, use *lsblk* before and after plugging in your SD card to identify it. You should end up with something a lot like this:

sdb
   sdb1
   sdb2

with sdb1 
being the FAT filesystem (boot) partition, 
and sdb2 being the ext4 filesystem (root) partition.


Mount these first, adjusting the partition letter as necessary:

mkdir mnt
mkdir mnt/fat32
mkdir mnt/ext4
sudo mount /dev/sdb1 mnt/fat32
sudo mount /dev/sdb2 mnt/ext4


NOTE
*You should adjust the drive letter appropriately for your setup, e.g. if your SD card appears as /dev/sdc instead of /dev/sdb.*


*Next, install the kernel modules onto the SD card:*
__For 32-bit__
sudo env PATH=$PATH make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- INSTALL_MOD_PATH=mnt/ext4 modules_install

__For 64-bit__
sudo env PATH=$PATH make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- INSTALL_MOD_PATH=mnt/ext4 modules_install


*Finally, copy the kernel and Device Tree blobs onto the SD card, making sure to back up your old kernel:*


__For 32-bit__

sudo cp mnt/fat32/$KERNEL.img mnt/fat32/$KERNEL-backup.img
sudo cp arch/arm/boot/zImage mnt/fat32/$KERNEL.img
# Choose one of the following based on the kernel version
  # For kernels up to 6.4:
  sudo cp arch/arm/boot/dts/*.dtb mnt/fat32/
  # For kernel 6.5 and above:
  sudo cp arch/arm/boot/dts/broadcom/*.dtb mnt/fat32/
sudo cp arch/arm/boot/dts/overlays/*.dtb* mnt/fat32/overlays/
sudo cp arch/arm/boot/dts/overlays/README mnt/fat32/overlays/
sudo umount mnt/fat32
sudo umount mnt/ext4

__For 64-bit__

sudo cp mnt/fat32/$KERNEL.img mnt/fat32/$KERNEL-backup.img
sudo cp arch/arm64/boot/Image mnt/fat32/$KERNEL.img
sudo cp arch/arm64/boot/dts/broadcom/*.dtb mnt/fat32/
sudo cp arch/arm64/boot/dts/overlays/*.dtb* mnt/fat32/overlays/
sudo cp arch/arm64/boot/dts/overlays/README mnt/fat32/overlays/

sudo umount mnt/fat32
sudo umount mnt/ext4
















#### nproc  查看核心数量

### build on rasp pi **LOCAL**

For Raspberry Pi 5 default 64-bit build configuration:


cd linux
KERNEL=kernel_2712
make bcm2712_defconfig

#### build 64bit
make -j4 Image.gz modules dtbs
sudo make modules_install

#### install 
sudo cp arch/arm64/boot/dts/broadcom/*.dtb /boot/firmware/
sudo cp arch/arm64/boot/dts/overlays/*.dtb* /boot/firmware/overlays/
sudo cp arch/arm64/boot/dts/overlays/README /boot/firmware/overlays/
sudo cp arch/arm64/boot/Image.gz /boot/firmware/$KERNEL.img