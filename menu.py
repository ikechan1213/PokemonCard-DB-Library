# タイトル表示
def show_title():
    pass

# メニュー表示
def show_menu():
    pass

# カードを1枚表示する
def show_card(card):
    pass

# カード一覧を表示する
def show_cards(cards):
    """カード一覧を表示する"""

    if not cards:
        print("カードが登録されていません。")
        return
    
    print("--- 登録済みカード一覧 ---")

    for card in cards:
        print(f"カード番号: {card.card_number}, パックID: {card.packid}, カード名: {card.name}, "
              f"進化: {card.evolution}, HP: {card.hp}, タイプ: {card.type}, "
              f"レアリティ: {card.rarity}, パック名: {card.pack}, 所持枚数: {card.count}")
        
# メッセージ表示
def show_message(message):
    print(message)

def pause():
    input("続行するにはEnterキーを押してください...")