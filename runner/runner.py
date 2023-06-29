import ansible_runner


def start_runner(playbook, inventory, emit_function=print):
    def status_handler(data, runner_config):
        print('STATUS -', data['status'])

    def event_handler(data):
        print('''
        --==--E-=-V-=-E-=-N-=-T--==--
        ''')

        if data['event'] == 'runner_on_ok':
            print('host', data['event_data']['host'], 'SUCCESS')
            emit_function(
                'message', {'data': f"host {data['event_data']['host']} SUCCESS"})
            if 'stdout_lines' in data['event_data']['res']:
                for i in data['event_data']['res']['stdout_lines'][0]:
                    print(i)

        if data['event'] == 'runner_on_failed':
            print('host', data['event_data']['host'], 'FAILED')
            print(data)

        if data['event'] == 'playbook_on_stats':
            final_stats = data['stdout'].split('\r\n')
            for i in final_stats:
                print(i)

    ansible_runner.run(event_handler=event_handler, status_handler=status_handler,
                       inventory=inventory, playbook=playbook)


inventory = '/home/ubuntu-admin/ansible_runner_gui/testHosts'
playbook = '/home/ubuntu-admin/ansible_runner_gui/getData.yml'

start_runner(playbook=playbook, inventory=inventory)
