Goals:
<br/>To automatically add 2 rows with the same string value, for this case to generate  on a Cisco router.
<br/>(show interface &lt;interface ID> | in CRC)

<br/>How to run the script:
<br/>1. Put the data_intf.txt in the same directory with triplicate_2.py
<br/>2. Open python terminal > hit python3 triplicate_2.py > enter
<br/>3. Extracted .txt file will prompt in the same directory, named with 3pli_{timestamp}.txt

Before:
<br/>show interface Te0/2/0/0  | in CRC
<br/>show interface Te0/2/0/1  | in CRC

After:
<br/>show interface Te0/2/0/0  | in CRC
<br/>show interface Te0/2/0/0  | in CRC
<br/>show interface Te0/2/0/0  | in CRC
<br/>show interface Te0/2/0/1  | in CRC
<br/>show interface Te0/2/0/1  | in CRC
<br/>show interface Te0/2/0/1  | in CRC
