import requests
from rich import print

API_KEY = "7ddc73a2-ae6f-4b1e-810f-e9e385404e46"
API_BASE_URL = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"

def main():
    while True:
        word = input("Enter a word (or type 'exit' to quit): ").strip()

        if word == "exit":
            print("[bold blue]Exiting the dictionary tool. Goodbye![/bold blue]")
            break

        response = requests.get(f"{API_BASE_URL}{word}", params={"key": API_KEY})

        if response.status_code != 200:
            print(f"[red]API error {response.status_code}[/red]")
            continue

        data = response.json()
        if not data:
            print("[bold red]No definitions found.[/bold red]")
            continue

        main_list = data[0]
        first_dict = main_list.get("hwi", {}).get("hw", word)
        pronunciation = main_list.get("hwi", {}).get("prs", [{}])[0].get("mw", "")
        part_of_speech = main_list.get("fl", "")
        defination = main_list.get("shortdef", [])

        print(f"\n[bold cyan]{first_dict}[/bold cyan] ({part_of_speech}) [italic]{pronunciation}[/italic] - [green]{defination}[/green]")
   
main()

