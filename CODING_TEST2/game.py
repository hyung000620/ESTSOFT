from googletrans import Translator

# Google 번역 API 초기화
translator = Translator()

# 5x5 배열 입력 받기
def get_word_grid():
    grid = []
    for i in range(5):
        row = input(f"5개의 글자를 입력하세요 (row {i + 1}): ")
        if len(row) != 5:
            print("각 행에 5개의 글자를 입력하세요.")
            return None
        grid.append(list(row.lower()))  # 입력된 문자열을 소문자로 변환하여 배열에 추가
    return grid

# 배열에서 모든 가능한 단어 목록 생성
def generate_words(grid):
    words = []
    for i in range(5):
        for j in range(5):
            for dx, dy in [(1, 0), (0, 1), (1, 1), (-1, 1)]:
                word = ""
                for k in range(5):
                    x, y = i + k * dx, j + k * dy
                    if 0 <= x < 5 and 0 <= y < 5:
                        word += grid[x][y]
                words.append(word)
    return words

# 영어 단어인지 확인하고 길이 반환
def is_english_word(word):
    try:
        translation = translator.translate(word, dest='en')
        return translation.src == 'en'
    except:
        return False

# 가장 긴 영어 단어 찾기
def find_longest_english_word(grid):
    words = generate_words(grid)
    longest_word = ""
    for word in words:
        if is_english_word(word) and len(word) > len(longest_word):
            longest_word = word
    return longest_word

# 메인 함수
def main():
    grid = get_word_grid()
    if grid:
        longest_word = find_longest_english_word(grid)
        print("5x5 배열:")
        for row in grid:
            print(" ".join(row))
        print("\n가장 긴 영어 단어:", longest_word)

if __name__ == "__main__":
    main()