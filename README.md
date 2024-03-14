# pes-db-generator
A collection of scripts to generate a database for the Pro Evolution Soccer series of games.

## Requirements
* Python 3.12+

## Quirks
### Pro Evolution Soccer 2019 
#### EDIT File
By default, when you generate a new EDIT file, the game for some reason doesn't include the player data.\
So it will always load the data from the database instead of modified EDIT data.\
It also crashes [the save editor](https://github.com/the4chancup/4ccEditor) due of no players being in the EDIT file.

In order to fix the EDIT file you need to:
1. Decrypt it with [pesXdecrypter](https://github.com/the4chancup/pesXdecrypter) using the `decrypter19.exe` executable.
2. Open `data.dat` file with your favourite hex editor.
3. Go to the `0x60` offset and set the player count necessary. In my case it's 5060 which is `0xC413` converted to hexadecimal.
4. Generate player edit data using the `player_edit_19.py` script.
5. Copy the data from the `Player_Edit.bin` file to the `0x7C` offset of `data.dat` and save.
6. Now encrypt it with [pesXdecrypter](https://github.com/the4chancup/pesXdecrypter) using the `encrypter19.exe` executable.\
You should now have a working EDIT file.

> [!NOTE]
> The hexadecimal in the EDIT file is using the little endian byte order.

> [!CAUTION]
> Make sure you replace existing bytes, don't insert new bytes.

### Pro Evolution Soccer 2015
#### Database
Using `Competition.bin`, `CompetitionKind.bin` and `CompetitionRegulation.bin` in the DLC crashes the game.
