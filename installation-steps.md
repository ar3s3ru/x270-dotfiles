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
