from internet import create_main_parser, comment, get_characters, graceful_exit


def main():
    main_parser = create_main_parser()
    main_args = main_parser.parse_args()
    address = f'http://{main_args.host}:{main_args.port}/'

    while True:
        try:
            cmd = input('Enter command(comment, get_characters, exit)\n')
            if cmd == 'comment':
                comment(address)
            elif cmd == 'get_characters':
                get_characters(address)
            elif cmd == 'exit':
                graceful_exit()
            else:
                print(f'Unknown command: {cmd}')
        except KeyboardInterrupt or EOFError:
            graceful_exit()


if __name__ == '__main__':
    main()
