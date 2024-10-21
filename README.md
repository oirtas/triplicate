Goals:
Added automatically 2 row with the same string value, for this case to generate (show interface &lt;interface> | in CRC) on a Cisco router.

Before:
show interface Te0/2/0/0  | in CRC
show interface Te0/2/0/1  | in CRC

After:
show interface Te0/2/0/0  | in CRC
show interface Te0/2/0/0  | in CRC
show interface Te0/2/0/0  | in CRC
show interface Te0/2/0/1  | in CRC
show interface Te0/2/0/1  | in CRC
show interface Te0/2/0/1  | in CRC
