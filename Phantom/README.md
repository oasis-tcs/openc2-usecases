# Phantom Use Cases

* all_actions_in_phantom.json - the current list of 1028 action-target pairs we can execute in Phantom across about 200 actuators (we call them apps). Most of them would probably be useful to support in OpenC2.
* 01.endpoint_list_processes.md - a simple action to evaluate as a thread and attempt to translate to OpenC2
* 02.endpoint_deny_process_with_hash.md - prevent processes from launching when the executable has the given hash (add to hash blacklist)
* 03.endpoint_stop_process_by_pid.md - terminate a process by its id
* 04.endpoint_delete_file.md - delete a file by its path
