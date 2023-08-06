from emojipasta.generator import EmojipastaGenerator
import emojipasta.util.cli as cli

def main():
    args = cli.parse_arguments()
    generator = EmojipastaGenerator.of_default_mappings()

    print(generator.generate_emojipasta(args.string_to_parse))
    
if __name__ == "__main__":
    main()