from net_utils import InternetUtils
from tk_utils import TKWrapper


def main():
    tk = TKWrapper()
    search_item, number_of_items, folder_path = tk.open_dialogue()

    net_u = InternetUtils(search_item=search_item)
    final_gifs = net_u.get_all_img_tags()

    net_u.files_downloader(number_of_items=number_of_items, folder_path=folder_path, final_gifs=final_gifs)

if __name__ == "__main__":
    main()


