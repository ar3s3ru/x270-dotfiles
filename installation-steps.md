Steps for Arch Linux installation for Thinkpad X270

1. Pre-install

	* Added keymap and locale
		```bash
		/etc/vconsole.conf
		-------------------
		KEYMAP=us-acentos
		```

2. Post-install


	* Installed `i3-gaps` from AUR
		* Configuration is in `.config/i3/config`
	* Generated SSH keys with ED25519 elliptic-curve protocol
		```bash
		ssh-keygen -t ed25519 <email>
		```
	* Added `udev` rule for Trackpoint
		* Reference found [here](https://wiki.archlinux.org/index.php/TrackPoint)
    * `neovim` config require Python library `neovim`
        ```bash
        # pip install neovim
        ```
    * Added `/usr/bin/alsa_name.pl` script and `udev` rule for sound card usage
      with ALSA
        * Reference link [here](https://alsa.opensrc.org/Udev#Example_to_map_USB_Ports_to_ALSA_card_numbers_and_add_each_sound_card_to_a_combined.2C_single_interface_device)
