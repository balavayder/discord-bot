BOT_TOKEN: str = ""
SPOTIFY_ID: str = ""
SPOTIFY_SECRET: str = ""
client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = ""

BOT_PREFIX = "!"

EMBED_COLOR = 0x4dd4d0

SUPPORTED_EXTENSIONS = ('.webm', '.mp4', '.mp3', '.avi', '.wav', '.m4v', '.ogg', '.mov')

MAX_SONG_PRELOAD = 5

COOKIE_PATH = "/cfg/cookies/cookies.txt"

GLOBAL_DISABLE_AUTOJOIN_VC = False

VC_TIMEOUT = 600
VC_TIMOUT_DEFAULT = True
ALLOW_VC_TIMEOUT_EDIT = True

STARTUP_MESSAGE = "Starting Bot..."
STARTUP_COMPLETE_MESSAGE = "Startup Complete"

NO_GUILD_MESSAGE = 'Error: Dołącz do VC'
USER_NOT_IN_VC_MESSAGE = "Error: Dołącz do aktywnego VC"
WRONG_CHANNEL_MESSAGE = "Error: Please use configured command channel"
NOT_CONNECTED_MESSAGE = "Error: Nie połączono z żadnym VC"
ALREADY_CONNECTED_MESSAGE = "Error: Już połączono z VC"
CHANNEL_NOT_FOUND_MESSAGE = "Error: Nie można znaleźć tego VC"
DEFAULT_CHANNEL_JOIN_FAILED = "Error: Nie można połączyć z default VC"
INVALID_INVITE_MESSAGE = "Error: Invalid invitation link"

INFO_HISTORY_TITLE = "Songs Played:"
MAX_HISTORY_LENGTH = 10
MAX_TRACKNAME_HISTORY_LENGTH = 15

SONGINFO_UPLOADER = "Uploader: "
SONGINFO_DURATION = "Długość: "
SONGINFO_SECONDS = "s"
SONGINFO_LIKES = "Łapki w górę: "
SONGINFO_DISLIKES = "Łapki w dół: "
SONGINFO_NOW_PLAYING = "Aktualnie grane"
SONGINFO_QUEUE_ADDED = "Dodano do kolejki"
SONGINFO_SONGINFO = "Song info"
SONGINFO_ERROR = "Error: content +18, nie działa na razie"
SONGINFO_PLAYLIST_QUEUED = "Zakolejkowano playliste :page_with_curl:"
SONGINFO_UNKNOWN_DURATION = "Unknown"

HELP_CONNECT_SHORT = "Łączy Balavaydera do aktualnego VC"
HELP_CONNECT_LONG = "Łączy Balavaydera do aktualnego VC"
HELP_DISCONNECT_SHORT = "RESET Balavaydera z VC"
HELP_DISCONNECT_LONG = "RESET Balavaydera z VC"

HELP_SETTINGS_SHORT = "Pokazuje i zmienia ustawienia Balavaydera"
HELP_SETTINGS_LONG = "Pokaż i zmień ustawienia Balavaydera na serwerze Usage: {}settings setting_name value".format(
    BOT_PREFIX)

HELP_HISTORY_SHORT = "Pokazuje historię piosenek"
HELP_HISTORY_LONG = "Pokazuje " + str(MAX_TRACKNAME_HISTORY_LENGTH) + " ostatnio granych piosenek"
HELP_PAUSE_SHORT = "Pauzuje muzyke"
HELP_PAUSE_LONG = "Pauza, wpisz ponownie aby kontynuować"
HELP_VOL_SHORT = "Zmień głośność %"
HELP_VOL_LONG = "Zmienia głośność granego audio, użyj % aby sprecyzować poziom głośności"
HELP_PREV_SHORT = "Zagraj poprzednia piosenke"
HELP_PREV_LONG = "Gra poprzednia piosenke jeszcze raz"
HELP_RESUME_SHORT = "Wznawia granie muzyki"
HELP_RESUME_LONG = "Wznawia granie muzyki przez Balavaydera"
HELP_SKIP_SHORT = "Skip song"
HELP_SKIP_LONG = "Skipuje aktualna piosenke i przechodzi do następnej"
HELP_SONGINFO_SHORT = "Info na temat aktualnej piosenki"
HELP_SONGINFO_LONG = "Detailed info na temat aktualnej piosenki"
HELP_STOP_SHORT = "Zatrzymuje muzykę i czyści kolejkę"
HELP_STOP_LONG = "Zatrzymuje muzykę i czyści kolejkę"
HELP_MOVE_LONG = f"{BOT_PREFIX}move [position] [new position]"
HELP_MOVE_SHORT = 'Przemieszcza piosenkę w kolejce'
HELP_YT_SHORT = "Link(spotify, sc, twitter, youtube) lub tytuł(youtube)"
HELP_YT_LONG = ("$p [link/video title/key words/playlist-link/soundcloud link/spotify link/bandcamp link/twitter link]")
HELP_PING_SHORT = "check"
HELP_PING_LONG = "TEST BOT RESPONSE"
HELP_CLEAR_SHORT = "Czyści kolejkę"
HELP_CLEAR_LONG = "Czyści kolejkę i skipuje aktualnie graną piosenkę"
HELP_LOOP_SHORT = "Zapętla aktualnie graną piosenkę, działą on/off"
HELP_LOOP_LONG = "Zapętla aktualnie graną piosenkę i 'blokuje' kolejkę, wpisz ponownie aby wznowić kolejkę"
HELP_QUEUE_SHORT = "Pokazuję piosenki w kolejce"
HELP_QUEUE_LONG = "Pokazuje liczbę piosenek w kolejce (max 10)"
HELP_SHUFFLE_SHORT = "Robi shuffle w kolejce"
HELP_SHUFFLE_LONG = "Losowo przestawia kolejność piosenek w playliście"
HELP_CHANGECHANNEL_SHORT = "Zmienia kanał na twój aktualny"
HELP_CHANGECHANNEL_LONG = "Zmienia kanał na aktualny"

ABSOLUTE_PATH = ''  # do not modify
