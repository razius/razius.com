Programing the STK600 AVR board on Linux using C
################################################
:date: 2012-09-27 10:51
:tags: avr, debian, linux, ubuntu
:slug: programing-the-stk600-avr-board-on-linux-using-c

Setting up the developing enviroment
------------------------------------

Note: I'm assuming you have a .deb based distribution and a AVR STK600 board with a ATmega2560 microcontroller that you are programming using an USB cable.

Installing the software
~~~~~~~~~~~~~~~~~~~~~~~

We need to install the following programs and their dependencies:

- gcc-avr: The GNU C compiler (cross compiler for avr)
- gdb-avr: The GNU Debugger for avr
- avr-libc: Standard C library for Atmel AVR development
- avrdude: Tool to download the compiled code and data to the Atmel AVR microcontroller

Install them by running the following command:

.. code-block:: console

    $ sudo apt-get install avrdude avrdude-doc gcc-avr binutils-avr avr-libc simulavr gdb-avr

Setting up the permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to download the firmware on the device as a regular user we need to setup some udev rules for device permissions otherwise we get the following errors:

.. code-block:: text

    avrdude: usb_open(): cannot read serial number...
    avrdude: usb_open(): cannot read product name...
    avrdude: usbdev_open(): error setting configuration 1...
    avrdude: usbdev_open(): did not find any USB device...

Create a new file under ``/etc/udev/rules.d/`` named ``41-atmega.rules`` with the following content:

.. code-block:: bash

    SUBSYSTEM=="usb", ATTR{idVendor}=="03eb", ATTR{idProduct}=="product_id", OWNER="my_username", GROUP="my_group", MODE="0666"

Where you need to replace ``product_id``, ``my_username`` and ``my_group`` with your own values.

``my_username`` is the username that you login to the system, you can find it by running the following command:

.. code-block:: console

    $ id -gn

``my_group`` is the primary group of your username, you can find it by running the following command:

.. code-block:: console

    $ id -un

``product_id`` is the USB Product ID assigned by the manufacturer, you can find it by running the following command:

.. code-block:: console

    $ lsusb |grep Atmel | awk '{ print $6 }' | awk 'BEGIN { FS = ":" } ; { print $2 }'

Reload udev to apply our rules:

.. code-block:: console

    $ sudo /etc/init.d/udev reload

Finally, be sure to disconnect and reconnect the AVR board for the new rule to be applied.

Creating a new project
----------------------

Create a new file named ``test.c`` with the following content:

.. code-block:: c

    /* Sample C program to turn on all leds on the AVR */

    #include <avr/io.h>

    int main(void) {
        DDRA = 0xFF;
        PORTA = ~0xFF;
        return 0;
    }

Create a new file named `Makefile`_ with the following content:

.. code-block:: makefile

    CC=`which avr-gcc`
    CFLAGS=-g -Os -Wall -mcall-prologues -std=c99 -mmcu=atmega2560
    OBJ2HEX=`which avr-objcopy`
    AVRD=`which avrdude`
    # Modify TARGET to match your C filename without the .c extension (it's test.c in this case)
    TARGET=test

    program : $(TARGET).hex
        $(AVRD) -p atmega2560 -c stk600 -P usb -v -v -U flash:w:$(TARGET).hex
    %.obj : %.o
        $(CC) $(CFLAGS) $< -o $@

    %.hex : %.obj
        $(OBJ2HEX) -R .eeprom -O ihex $< $@

    clean :
        rm -f *.hex *.obj *.o

Now all you have to do is run ``make`` in the project folder to build the binary and upload it to the AVR Board:

.. code-block:: console

    $ make

.. _Makefile: http://en.wikipedia.org/wiki/Make_(software)#Makefiles
