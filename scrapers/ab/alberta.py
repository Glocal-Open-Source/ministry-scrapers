import ab_agencies
import ab_ministries

def main() -> None:
    ab_agencies.scrape_all_agencies()
    ab_ministries.scrape_ministries()
    

if __name__ == "__main__":
    main()
