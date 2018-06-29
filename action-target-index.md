## Actions
| ID | Property Name | Use Case Source |
|:---|:---|:---|
| 1 | **scan** | [Symantec: scan>>file](Symantec/process_anti_virus_scanner_scan_file.md)
| 2 | **locate** | [ATT: locate>>ip_addr](ATT/03.locate.md)<br>[Symantec: locate>>process](Symantec/endpoint_locate_process.md)<br>[Symantec: locate>>directory](Symantec/process_anti_virus_scanner_locate_directory.md)<br>[Symantec: locate>>file](Symantec/process_anti_virus_scanner_locate_file.md)<br>[Symantec: locate>>windows_registry_key](Symantec/process_anti_virus_scanner_locate_windows_registry_key.md)
| 3 | **query** | [General: query>>property](General/Example_%20get__property.md)<br>[Phantom: query>>process](Phantom/01.endpoint_list_process.md)<br>[sFractalConsulting: query>>openc2](sFractalconsulting/24.version.md)<br>[General: query>>openc2](https://docs.google.com/document/d/1vF7e9Mp_45u-RuPrbRiIoIUcOmoDCkKEAcJKCr6tvgA/edit?usp=sharing)<br>[Symantec: query>>device](Symantec/endpoint_query_device.md)<br>[Symantec: query>>device](Symantec/endpoint_query_device.md)<br>[Symantec: query>>software](Symantec/endpoint_query_software.md)<br>[Symantec: query>>url](Symantec/network_proxy_query_url.md)
| 4 | ~~report~~ | 
| 5 | ~~notify~~ | 
| 6 | **deny** | [ATT: deny>>ip_connection](ATT/04.deny.md)<br>[Phantom: deny>>process](Phantom/02.endpoint_deny_process_with_hash.md)<br>[STIX: deny>>ip_connection](STIX/01.ipv4_cidr.md)<br>[sFractalConsulting: deny>>ip_connection](sFractalconsulting/01.sensing.md)<br>[sFractalConsulting: deny>>domain_name](sFractalconsulting/20.bad_url.md)<br>[LG: deny>>ip_addr](https://docs.google.com/document/d/1TNOwlpFrip29_1lGNW2xIV6GyOZe83J96C2DxdgOwME/edit?usp=sharing)<br>[Symantec: deny>>file](Symantec/endpoint_deny_file.md)<br>[Symantec: deny>>process](Symantec/endpoint_deny_process.md)<br>[Symantec: deny>>url](Symantec/network_proxy_deny_url.md)<br>[Symantec: deny>>email-addr](Symantec/process_email_service_deny_email-addr.md)<br>[Symantec: deny>>email-message](Symantec/process_email_service_deny_email-message.md)
| 7 | **contain** | [ATT: contain>>domain_name](ATT/01.contain.md)<br>[STIX: contain>>device](STIX/04.quarantive_exfil.md)<br>[Symantec: contain>>device](Symantec/endpoint_contain_device.md)
| 8 | **allow** | [ATT: allow>>domain_name](ATT/02.allow.md)<br>[ATT: allow>>ip_connection](ATT/05.allow.md)<br>[sFractalConsulting: allow>>ip_connection](sFractalconsulting/02.another_user.md)<br>[Symantec: allow>>device](Symantec/endpoint_allow_device.md)<br>[Symantec: allow>>file](Symantec/endpoint_allow_file.md)<br>[Symantec: allow>>url](Symantec/endpoint_allow_url.md)
| 9 | **start** | [Symantec: start>>process](Symantec/endpoint_start_process.md)<br>[sFractal: start: vm](sFractalConsulting/25.create_vm.md)
| 10 | **stop** | [Phantom: stop>>process](Phantom/03.endpoint_stop_process_by_pid.md)<br>[Symantec: stop>>process](Symantec/endpoint_stop_process.md)<br>[sFractal: stop: vm](sFractalConsulting/25.create_vm.md)
| 11 | **restart** | [Symantec: restart>>device](Symantec/endpoint_restart_device.md)<br>[Symantec: restart>>process](Symantec/endpoint_restart_process.md)
| 12 | ~~pause~~ | 
| 13 | ~~resume~~ | 
| 14 | **cancel** | [Symantec: cancel>>openc2>>command](Symantec/endpoint_cancel_command.md)
| 15 | ~~set~~ | 
| 16 | **update** | [sFractalConsulting: update>>software](sFractalconsulting/18.no_resp_update_sw.md)<br>[sFractalConsulting: update>>software](sFractalconsulting/19.resp_update_sw.md)<br>[Symantec: update>>device](Symantec/endpoint_update_device.md)<br>[Symantec: update>>software](Symantec/endpoint_update_software.md)
| 17 | ~~move~~ | 
| 18 | **redirect** | [STIX: redirect>>ip_connection](STIX/02.dns_lookup.md)<br>[LG: redirect>>domain_name](https://docs.google.com/document/d/19qIzUhDtVAkH_dSFBpK4iHLkk2ohAOk3hF0TbZxiePU/edit?usp=sharing)<br>[LG: redirect>>url](https://docs.google.com/document/d/1qh_pcoYNofAleh20vtohSQ0VURhlGDB30-ZOpifFSWo/edit?usp=sharing)
| 19 | ~~create~~ | 
| 20 | **delete** | [Phantom: delete>>file](Phantom/04.endpoint_delete_file.md)<br>[STIX: delete>>artifact](STIX/03.malware_hash.md)<br>[sFractalConsulting: delete>>process](sFractalconsulting/17.no_resp_procid.md)<br>[sFractalConsulting: delete>>email_message](sFractalconsulting/21.bad_email.md)<br>[sFractalConsulting: delete>>file](sFractalconsulting/22.bad_file.md)<br>[Phantom: delete>>file](https://docs.google.com/document/d/1oBy8y7GPuG1zz_6PiPwt6VHDu1NHNf_qD8fb8jxIFG8/edit?usp=sharing)<br>[Symantec: delete>>device](Symantec/endpoint_delete_device.md)<br>[Symantec: delete>>file](Symantec/endpoint_delete_file.md)
| 21 | ~~snapshot~~ | 
| 22 | **detonate** | [Symantec: detonate>>file](Symantec/process_sandbox_detonate_file.md)<br>[Symantec: detonate>>url](Symantec/process_sandbox_detonate_url.md)
| 23 | **restore** | [Symantec: restore>>file](Symantec/process_anti_virus_scanner_restore_file.md)
| 24 | ~~save~~ | 
| 25 | ~~throttle~~ | 
| 26 | ~~delay~~ | 
| 27 | ~~substitute~~ | 
| 28 | **copy** | [Symantec: copy>>file](Symantec/endpoint_copy_file.md)
| 29 | ~~sync~~ | 
| 30 | **investigate** | [Symantec: investigate>>device](Symantec/endpoint_investigate_device.md)
| 31 | ~~mitigate~~ | 
| 32 | **remediate** | [Symantec: remediate>>file](Symantec/endpoint_remediate_file.md)

## Targets
| ID | Property Name | Type | Use Case Source |
|:---|:---|:---|:---|
| 1 | **artifact** | Artifact | [STIX: delete>>artifact](STIX/03.malware_hash.md)
| 2 | **command** | **Command** | [Symantec: cancel>>command](Symantec/endpoint_cancel_command.md) 
| 3 | **device** | Device | [STIX: contain>>device](STIX/04.quarantive_exfil.md)<br>[Symantec: allow>>device](Symantec/endpoint_allow_device.md)<br>[Symantec: delete>>device](Symantec/endpoint_delete_device.md)<br>[Symantec: query>>device](Symantec/endpoint_query_device.md)<br>[Symantec: restart>>device](Symantec/endpoint_restart_device.md)<br>[Symantec: update>>device](Symantec/endpoint_update_device.md)<br>[Symantec: contain>>device](Symantec/endpoint_contain_device.md)
| 4 | **directory** | Directory | [Symantec: locate>>directory](Symantec/process_anti_virus_scanner_locate_directory.md)
| 5 | ~~disk~~ | ~~Disk~~ | 
| 6 | ~~disk_partition~~ | ~~Disk-Partition~~ | 
| 7 | **domain_name** | Domain-Name | [ATT: contain>>domain_name](ATT/01.contain.md)<br>[ATT: allow>>domain_name](ATT/02.allow.md)<br>[sFractalConsulting: deny>>domain_name](sFractalconsulting/20.bad_url.md)<br>[LG: redirect>>domain_name](https://docs.google.com/document/d/19qIzUhDtVAkH_dSFBpK4iHLkk2ohAOk3hF0TbZxiePU/edit?usp=sharing)
| 8 | **email_addr** | Email-Addr | [Symantec: deny>>email-addr](Symantec/process_email_service_deny_email-addr.md)
| 9 | **email_message** | Email-Message | [sFractalConsulting: delete>>email_message](sFractalconsulting/21.bad_email.md)<br><br>[Symantec: deny>>email-message](Symantec/process_email_service_deny_email-message.md)
| 10 | **file** | File | [Phantom: delete>>file](Phantom/04.endpoint_delete_file.md)<br>[sFractalConsulting: delete>>file](sFractalconsulting/22.bad_file.md)<br>[Phantom: delete>>file](https://docs.google.com/document/d/1oBy8y7GPuG1zz_6PiPwt6VHDu1NHNf_qD8fb8jxIFG8/edit?usp=sharing)<br>[Symantec: allow>>file](Symantec/endpoint_allow_file.md)<br>[Symantec: copy>>file](Symantec/endpoint_copy_file.md)<br>[Symantec: delete>>file](Symantec/endpoint_delete_file.md)<br>[Symantec: deny>>file](Symantec/endpoint_deny_file.md)<br>[Symantec: remediate>>file](Symantec/endpoint_remediate_file.md)<br>[Symantec: locate>>file](Symantec/process_anti_virus_scanner_locate_file.md)<br>[Symantec: restore>>file](Symantec/process_anti_virus_scanner_restore_file.md)<br>[Symantec: scan>>file](Symantec/process_anti_virus_scanner_scan_file.md)<br>[Symantec: detonate>>file](Symantec/process_sandbox_detonate_file.md)
| 11 | **ip_addr** | IP-Addr | [ATT: locate>>ip_addr](ATT/03.locate.md)<br>[LG: deny>>ip_addr](https://docs.google.com/document/d/1TNOwlpFrip29_1lGNW2xIV6GyOZe83J96C2DxdgOwME/edit?usp=sharing)
| 13 | ~~mac_addr~~ | ~~Mac-Addr~~ | 
| 14 | ~~memory~~ | ~~Memory~~ | 
| 15 | **ip_connection** | IP-Connection | [ATT: deny>>ip_connection](ATT/04.deny.md)<br>[ATT: allow>>ip_connection](ATT/05.allow.md)<br>[STIX: deny>>ip_connection](STIX/01.ipv4_cidr.md)<br>[STIX: redirect>>ip_connection](STIX/02.dns_lookup.md)<br>[sFractalConsulting: allow>>ip_connection](sFractalconsulting/01.another_user.md)<br>[sFractalConsulting: deny>>ip_connection](sFractalconsulting/02.sensing.md)
| 16 | **openc2** | OpenC2 | [sFractalConsulting: query>>openc2](sFractalconsulting/24.version.md)<br>[General: query>>openc2](https://docs.google.com/document/d/1vF7e9Mp_45u-RuPrbRiIoIUcOmoDCkKEAcJKCr6tvgA/edit?usp=sharing)<br>[Symantec: cancel>>openc2>>command](Symantec/endpoint_cancel_command.md)
| 17 | **process** | Process | [Phantom: query>>process](Phantom/01.endpoint_list_process.md)<br> [Phantom: deny>>process](Phantom/02.endpoint_deny_process_with_hash.md)<br> [Phantom: stop>>process](Phantom/03.endpoint_stop_process_by_pid.md)<br>[sFractalConsulting: delete>>process](sFractalconsulting/17.no_resp_procid.md)<br>[Symantec: deny>>process](Symantec/endpoint_deny_process.md)<br>[Symantec: locate>>process](Symantec/endpoint_locate_process.md)<br>[Symantec: restart>>process](Symantec/endpoint_restart_process.md)<br>[Symantec: stop>>process](Symantec/endpoint_stop_process.md)<br>[Symantec: start>>process](Symantec/endpoint_start_process.md)
| 25 | **property** | Property | [General: query>>property](General/Example_%20get__property.md)
| 18 | **software** | Software | [sFractalConsulting: update>>software](sFractalconsulting/18.no_resp_update_sw.md)<br>[sFractalConsulting: update>>software](sFractalconsulting/19.resp_update_sw.md)<br>[Symantec: query>>software](Symantec/endpoint_query_software.md)<br>[Symantec: update>>software](Symantec/endpoint_update_software.md)
| 19 | **url** | Url | [LG: redirect>>url](https://docs.google.com/document/d/1qh_pcoYNofAleh20vtohSQ0VURhlGDB30-ZOpifFSWo/edit?usp=sharing)<br>[Symantec: query>>url](Symantec/network_proxy_query_url.md)<br>[Symantec: deny>>url](Symantec/network_proxy_deny_url.md)<br>[Symantec: allow>>url](Symantec/endpoint_allow_url.md)<br>[Symantec: detonate>>url](Symantec/process_sandbox_detonate_url.md)
| 20 | ~~user_account~~ | ~~User-Account~~ | 
| 21 | ~~user_session~~ | ~~User-Session~~ | 
| 22 | ~~volume~~ | ~~Volume~~ | 
| 23 | **windows_registry_key** | Windows-Registry-Key | [Symantec: locate>>windows_registry_key](Symantec/process_anti_virus_scanner_locate_windows_registry_key.md)
| 24 | ~~x509_certificate~~ | ~~X509-Certificate~~ | 
| 1024 | ~~slpff~~ | ~~Slpff-Target~~ | 
