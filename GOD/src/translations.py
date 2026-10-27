"""
Fichier de traductions pour GOD (God Offers Downloads)
Organisé par catégories logiques
"""


def get_text(key, lang="fr", **kwargs):
    """
    Récupère le texte traduit pour une clé donnée

    Args:
        key: Clé de traduction
        lang: Langue (fr ou en)
        **kwargs: Arguments pour le formatage des chaînes

    Returns:
        str: Texte traduit
    """
    try:
        text = TRANSLATIONS[lang].get(key, TRANSLATIONS["fr"].get(key, key))
        if kwargs:
            return text.format(**kwargs)
        return text
    except (KeyError, AttributeError):
        return key


TRANSLATIONS = {
    # ============================================================
    # 🇫🇷 FRANÇAIS
    # ============================================================
    "fr": {
        # ──────────────────────────────────────────────────────
        # EN-TÊTE APPLICATION
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "Une interface graphique universelle pour le téléchargement de médias, optimisée par yt-dlp",

        # ──────────────────────────────────────────────────────
        # ONGLETS PRINCIPAUX
        # ──────────────────────────────────────────────────────
        "single_download_tab": "Téléchargement unique",
        "batch_download_tab": "Téléchargement par lot",
        "tutorial": "Tutoriel",

        # ──────────────────────────────────────────────────────
        # BOUTONS ET ACTIONS
        # ──────────────────────────────────────────────────────
        "check_button": "Ajouter",
        "download_button": "Télécharger",
        "cancel_button": "Annuler",
        "clear_queue": "Vider la file",
        "browse_button": "Parcourir",
        "load_from_file_button": "Charger depuis un fichier",
        "paste_multiple_urls": "Coller plusieurs URLs",
        "add_urls": "Ajouter",
        "max_concurrent_downloads": "Téléchargements simultanés max :",

        # ──────────────────────────────────────────────────────
        # CHAMPS ET LABELS
        # ──────────────────────────────────────────────────────
        "url_placeholder": "Collez l'URL YouTube ici",
        "paste_multiple_urls_hint": "Collez une URL par ligne :",
        "type_label": "Type :",
        "video_option": "Vidéo + Audio",
        "audio_only_option": "Audio uniquement",
        "resolution_label": "Résolution :",
        "audio_bitrate_label": "Bitrate audio :",
        "audio_format_label": "Format audio :",
        "output_folder_label": "Dossier de sortie :",
        "urls_list_label": "Liste des URLs YouTube (une par ligne) :",

        # ──────────────────────────────────────────────────────
        # INFORMATIONS VIDÉO
        # ──────────────────────────────────────────────────────
        "title": "Titre",
        "author": "Auteur",
        "upload_date": "Date de publication",
        "duration": "Durée",
        "views": "Vues",
        "likes": "Likes",
        "video_id": "ID vidéo",
        "url": "URL",
        "description": "Description",
        "no_description": "Aucune description.",
        "available_formats": "Formats disponibles",
        "best_video_format": "Meilleur format vidéo seule : ",
        "best_audio_format": "Meilleur format audio seul : ",

        # ──────────────────────────────────────────────────────
        # POPUP INFOS VIDÉO
        # ──────────────────────────────────────────────────────
        "video_info_title": "Informations vidéo",
        "text_summary": "Résumé texte",
        "tab": "Tableau",
        "detailed_summary": "Résumé détaillé",

        # ──────────────────────────────────────────────────────
        # STATUTS ET MESSAGES D'ÉTAT
        # ──────────────────────────────────────────────────────
        "ready_status": "Prêt",
        "loading_video_info": "Récupération des informations de la vidéo",
        "loading": "⏳ Chargement en cours...",
        "checking_url": "Vérification de l'URL...",
        "download_started": "Téléchargement démarré",
        "downloading": "Téléchargement :",
        "remaining_time": "Temps restant :",
        "processing_file": "Traitement du fichier...",
        "canceling_download": "Annulation du téléchargement...",
        "canceling_batch_download": "Annulation du téléchargement par lot...",
        "no_file_in_the_queue": "Aucun fichier dans la file d'attente",

        # ──────────────────────────────────────────────────────
        # PLAYLISTS
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 Playlist détectée : {count} vidéo trouvée. Chargement...",
        "playlist_detected_plural": "📋 Playlist détectée : {count} vidéos trouvées. Chargement...",
        "queue_added_singular": "✅ {count} vidéo ajoutée à la file d'attente",
        "queue_added_plural": "✅ {count} vidéos ajoutées à la file d'attente",

        # ──────────────────────────────────────────────────────
        # MESSAGES DE SUCCÈS
        # ──────────────────────────────────────────────────────
        "download_complete": "Téléchargement terminé",
        "download_complete_message": "Le téléchargement a été complété avec succès !",
        "batch_download_complete": "Téléchargement par lot terminé",
        "downloads_success_ratio_singular": "✅ {success}/{total} téléchargement réussi",
        "downloads_success_ratio_plural": "✅ {success}/{total} téléchargements réussis",

        # ──────────────────────────────────────────────────────
        # MESSAGES D'ERREUR ET AVERTISSEMENTS
        # ──────────────────────────────────────────────────────
        "warning": "Attention",
        "error": "Erreur",
        "error_prefix": "Erreur : ",
        "download_failed": "Échec du téléchargement",
        "download_canceled": "Téléchargement annulé",
        "partial_download_message": "Certains fichiers n'ont pas été téléchargés",
        "enter_valid_url": "Veuillez entrer une URL valide",
        "no_valid_urls": "Aucune URL valide trouvée",
        "no_video": "Aucune vidéo trouvée dans cette URL",
        "no_resolutions_found": "Pas de résolutions trouvées",
        "no_bitrates_found": "Pas de bitrates trouvées",
        "fetching_impossible": "Impossible d'obtenir les informations de la vidéo",
        "playlist_private": "Playlist privée — connexion requise. Veuillez fournir des cookies YouTube.",

        # ──────────────────────────────────────────────────────
        # FICHIERS
        # ──────────────────────────────────────────────────────
        "select_output_folder": "Sélectionner un dossier de sortie",
        "select_cookies_file": "Sélectionner le fichier cookies.txt",
        "load_urls_list": "Charger une liste d'URLs",
        "text_files": "Fichiers texte",
        "loaded_urls": "Chargé {count} URLs depuis le fichier",
        "file_load_error": "Erreur lors du chargement du fichier : {error}",
        "cannot_read_file": "Impossible de lire le fichier : {error}",
        "download_folder": "Téléchargements",
    },

    # ============================================================
    # 🏴 BREZHONEG
    # ============================================================
    "br": {
        # ──────────────────────────────────────────────────────
        # PENN AR POELLAD
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "Un etrefas grafek hollvedel evit pellgargañ mediaoù, gwellaet gant yt-dlp",

        # ──────────────────────────────────────────────────────
        # IVINELLOÙ PENNAÑ
        # ──────────────────────────────────────────────────────
        "single_download_tab": "Pellgargañ unan",
        "batch_download_tab": "Pellgargañ a-stroll",
        "tutorial": "Sturlevr",

        # ──────────────────────────────────────────────────────
        # BOUTONOÙ HAG OBEREREZHIOÙ
        # ──────────────────────────────────────────────────────
        "check_button": "Ouzhpennañ",
        "download_button": "Pellgargañ",
        "cancel_button": "Nullañ",
        "clear_queue": "Goullonderiñ al lostenn",
        "browse_button": "Furchal",
        "load_from_file_button": "Kargañ diouzh ur restr",
        "paste_multiple_urls": "Pegañ meur a URL",
        "add_urls": "Ouzhpennañ",

        # ──────────────────────────────────────────────────────
        # MAEZIOÙ HA SKRIVELLOÙ
        # ──────────────────────────────────────────────────────
        "url_placeholder": "Pegit amañ URL YouTube",
        "paste_multiple_urls_hint": "Pegit un URL dre linenn:",
        "type_label": "Seurt:",
        "video_option": "Video + Son",
        "audio_only_option": "Son hepken",
        "resolution_label": "Pizhder:",
        "audio_bitrate_label": "Bitrate son:",
        "audio_format_label": "Furmad son:",
        "output_folder_label": "Kavlec'h ec'hankañ:",
        "urls_list_label": "Roll URL YouTube (unan dre linenn):",

        # ──────────────────────────────────────────────────────
        # TITOUROÙ AR VIDEO
        # ──────────────────────────────────────────────────────
        "title": "Titl",
        "author": "Aozer",
        "upload_date": "Deiziad embann",
        "duration": "Pad",
        "views": "Selladoù",
        "likes": "Plijadurioù",
        "video_id": "ID video",
        "url": "URL",
        "description": "Deskrivadur",
        "no_description": "Deskrivadur ebet.",
        "available_formats": "Furmadoù hegerz",
        "best_video_format": "Furmad video gwellañ hepken:",
        "best_audio_format": "Furmad son gwellañ hepken:",

        # ──────────────────────────────────────────────────────
        # PRENESTR TITOUROÙ AR VIDEO
        # ──────────────────────────────────────────────────────
        "video_info_title": "Titouroù ar video",
        "text_summary": "Diverradur testenn",
        "tab": "Taolenn",
        "detailed_summary": "Diverradur munudet",

        # ──────────────────────────────────────────────────────
        # STADIOÙ HA KEMENNADENNOÙ STAD
        # ──────────────────────────────────────────────────────
        "ready_status": "Prest",
        "loading_video_info": "O kerc'hat titouroù ar video",
        "loading": "⏳ O kargañ...",
        "checking_url": "O wiriañ an URL...",
        "download_started": "Ar pellgargañ zo kroget",
        "downloading": "O pellgargañ:",
        "remaining_time": "Amzer a chom:",
        "processing_file": "O tretan ar restr...",
        "canceling_download": "O nullañ ar pellgargañ...",
        "canceling_batch_download": "O nullañ ar pellgargañ a-stroll...",
        "no_file_in_the_queue": "Restr ebet el lostenn",

        # ──────────────────────────────────────────────────────
        # ROLLOÙ LENNAÑ
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 Roll-lenn kavet: 1 video kavet. O kargañ...",
        "playlist_detected_plural": "📋 Roll-lenn kavet: {count} video kavet. O kargañ...",
        "queue_added_singular": "✅ 1 video ouzhpennet d'al lostenn",
        "queue_added_plural": "✅ {count} video ouzhpennet d'al lostenn",

        # ──────────────────────────────────────────────────────
        # KEMENNADENNOÙ A-FET DEDENN
        # ──────────────────────────────────────────────────────
        "download_complete": "Pellgargañ echu",
        "download_complete_message": "Graet eo bet ar pellgargañ gant berzh!",
        "batch_download_complete": "Pellgargañ a-stroll echu",
        "downloads_success_ratio_singular": "✅ {success}/{total} pellgargañ berzhus",
        "downloads_success_ratio_plural": "✅ {success}/{total} pellgargañ berzhus",

        # ──────────────────────────────────────────────────────
        # KEMENNADENNOÙ FAZI HA DIWALL
        # ──────────────────────────────────────────────────────
        "warning": "Diwall",
        "error": "Fazi",
        "error_prefix": "Fazi: ",
        "download_failed": "C'hwitet eo ar pellgargañ",
        "download_canceled": "Nullet eo ar pellgargañ",
        "partial_download_message": "N'eo ket bet pellgarget lod eus ar restroù",
        "enter_valid_url": "Lakait un URL talvoudek mar plij",
        "no_valid_urls": "URL talvoudek ebet kavet",
        "no_video": "Video ebet kavet evit an URL-mañ",
        "no_resolutions_found": "Pizhder ebet kavet",
        "no_bitrates_found": "Bitrate ebet kavet",
        "fetching_impossible": "N'haller ket tapout titouroù ar video",
        "playlist_private": "Roll-lenn prevez — ret eo kevreañ. Pourchasit ar cookies YouTube.",

        # ──────────────────────────────────────────────────────
        # RESTROÙ
        # ──────────────────────────────────────────────────────
        "select_output_folder": "Dibabit ur c'havlec'h ec'hankañ",
        "select_cookies_file": "Dibabit restr cookies.txt",
        "load_urls_list": "Kargañ ur roll URL",
        "text_files": "Restroù testenn",
        "loaded_urls": "{count} URL karget diouzh ar restr",
        "file_load_error": "Fazi e-pad kargañ ar restr: {error}",
        "cannot_read_file": "N'haller ket lenn ar restr: {error}",
        "download_folder": "Pellgargadennoù",
    },

    # ============================================================
    # 🇬🇧 ENGLISH
    # ============================================================
    "en": {
        # ──────────────────────────────────────────────────────
        # APPLICATION HEADER
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "A universal media downloader GUI powered by yt-dlp",

        # ──────────────────────────────────────────────────────
        # MAIN TABS
        # ──────────────────────────────────────────────────────
        "single_download_tab": "Single Download",
        "batch_download_tab": "Batch Download",
        "tutorial": "Tutorial",

        # ──────────────────────────────────────────────────────
        # BUTTONS AND ACTIONS
        # ──────────────────────────────────────────────────────
        "check_button": "Add",
        "download_button": "Download",
        "cancel_button": "Cancel",
        "clear_queue": "Clear queue",
        "browse_button": "Browse",
        "load_from_file_button": "Load from file",
        "paste_multiple_urls": "Paste multiple URLs",
        "add_urls": "Add",
        "max_concurrent_downloads": "Max simultaneous downloads:",

        # ──────────────────────────────────────────────────────
        # FIELDS AND LABELS
        # ──────────────────────────────────────────────────────
        "url_placeholder": "Paste YouTube URL here",
        "paste_multiple_urls_hint": "Paste one URL per line:",
        "type_label": "Type:",
        "video_option": "Video + Audio",
        "audio_only_option": "Audio only",
        "resolution_label": "Resolution:",
        "audio_bitrate_label": "Audio bitrate:",
        "audio_format_label": "Audio format:",
        "output_folder_label": "Output folder:",
        "urls_list_label": "YouTube URLs list (one per line):",

        # ──────────────────────────────────────────────────────
        # VIDEO INFORMATION
        # ──────────────────────────────────────────────────────
        "title": "Title",
        "author": "Author",
        "upload_date": "Upload date",
        "duration": "Duration",
        "views": "Views",
        "likes": "Likes",
        "video_id": "Video ID",
        "url": "URL",
        "description": "Description",
        "no_description": "No description.",
        "available_formats": "Available formats",
        "best_video_format": "Best video-only format: ",
        "best_audio_format": "Best audio-only format: ",

        # ──────────────────────────────────────────────────────
        # VIDEO INFO POPUP
        # ──────────────────────────────────────────────────────
        "video_info_title": "Video information",
        "text_summary": "Text summary",
        "tab": "Table",
        "detailed_summary": "Detailed summary",

        # ──────────────────────────────────────────────────────
        # STATUS AND STATE MESSAGES
        # ──────────────────────────────────────────────────────
        "ready_status": "Ready",
        "loading_video_info": "Fetching video information",
        "loading": "⏳ Loading...",
        "checking_url": "Checking URL...",
        "download_started": "Download started",
        "downloading": "Downloading:",
        "remaining_time": "Remaining time:",
        "processing_file": "Processing file...",
        "canceling_download": "Canceling download...",
        "canceling_batch_download": "Canceling batch download...",
        "no_file_in_the_queue": "No file in the queue",

        # ──────────────────────────────────────────────────────
        # PLAYLISTS
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 Playlist detected: {count} video found. Loading...",
        "playlist_detected_plural": "📋 Playlist detected: {count} videos found. Loading...",
        "queue_added_singular": "✅ {count} video added to queue",
        "queue_added_plural": "✅ {count} videos added to queue",

        # ──────────────────────────────────────────────────────
        # SUCCESS MESSAGES
        # ──────────────────────────────────────────────────────
        "download_complete": "Download Complete",
        "download_complete_message": "Download completed successfully!",
        "batch_download_complete": "Batch Download Complete",
        "downloads_success_ratio_singular": "✅ {success}/{total} download successful",
        "downloads_success_ratio_plural": "✅ {success}/{total} downloads successful",

        # ──────────────────────────────────────────────────────
        # ERROR AND WARNING MESSAGES
        # ──────────────────────────────────────────────────────
        "warning": "Warning",
        "error": "Error",
        "error_prefix": "Error: ",
        "download_failed": "Download failed",
        "download_canceled": "Download canceled",
        "partial_download_message": "Some files were not downloaded",
        "enter_valid_url": "Please enter a valid URL",
        "no_valid_urls": "No valid URLs found",
        "no_video": "No video found at this URL",
        "no_resolutions_found": "No resolutions found",
        "no_bitrates_found": "No bitrates found",
        "fetching_impossible": "Unable to obtain video information",
        "playlist_private": "Private playlist — login required. Please provide YouTube cookies.",

        # ──────────────────────────────────────────────────────
        # FILES
        # ──────────────────────────────────────────────────────
        "select_output_folder": "Select output folder",
        "select_cookies_file": "Select cookies.txt file",
        "load_urls_list": "Load URLs list",
        "text_files": "Text files",
        "loaded_urls": "Loaded {count} URLs from file",
        "file_load_error": "Error loading file: {error}",
        "cannot_read_file": "Cannot read file: {error}",
        "download_folder": "Downloads",
    },

    # ============================================================
    # 🇪🇸 ESPAÑOL
    # ============================================================
    "es": {
        # ──────────────────────────────────────────────────────
        # ENCABEZADO DE APLICACIÓN
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "Una interfaz gráfica de usuario universal para descargar archivos multimedia con tecnología yt-dlp",

        # ──────────────────────────────────────────────────────
        # PESTAÑAS PRINCIPALES
        # ──────────────────────────────────────────────────────
        "single_download_tab": "Descarga única",
        "batch_download_tab": "Descarga por lotes",
        "tutorial": "Tutorial",

        # ──────────────────────────────────────────────────────
        # BOTONES Y ACCIONES
        # ──────────────────────────────────────────────────────
        "check_button": "Añadir",
        "download_button": "Descargar",
        "cancel_button": "Cancelar",
        "clear_queue": "Vaciar cola",
        "browse_button": "Explorar",
        "load_from_file_button": "Cargar desde archivo",
        "paste_multiple_urls": "Pegar varias URLs",
        "add_urls": "Añadir",

        # ──────────────────────────────────────────────────────
        # CAMPOS Y ETIQUETAS
        # ──────────────────────────────────────────────────────
        "url_placeholder": "Pega la URL de YouTube aquí",
        "paste_multiple_urls_hint": "Pega una URL por línea:",
        "type_label": "Tipo:",
        "video_option": "Vídeo + Audio",
        "audio_only_option": "Solo audio",
        "resolution_label": "Resolución:",
        "audio_bitrate_label": "Bitrate de audio:",
        "audio_format_label": "Formato de audio:",
        "output_folder_label": "Carpeta de destino:",
        "urls_list_label": "Lista de URLs de YouTube (una por línea):",

        # ──────────────────────────────────────────────────────
        # INFORMACIÓN DEL VÍDEO
        # ──────────────────────────────────────────────────────
        "title": "Título",
        "author": "Autor",
        "upload_date": "Fecha de publicación",
        "duration": "Duración",
        "views": "Vistas",
        "likes": "Me gusta",
        "video_id": "ID del vídeo",
        "url": "URL",
        "description": "Descripción",
        "no_description": "Sin descripción.",
        "available_formats": "Formatos disponibles",
        "best_video_format": "Mejor formato solo vídeo: ",
        "best_audio_format": "Mejor formato solo audio: ",

        # ──────────────────────────────────────────────────────
        # POPUP DE INFO DE VÍDEO
        # ──────────────────────────────────────────────────────
        "video_info_title": "Información del vídeo",
        "text_summary": "Resumen de texto",
        "tab": "Tabla",
        "detailed_summary": "Resumen detallado",

        # ──────────────────────────────────────────────────────
        # ESTADO Y MENSAJES DE ESTADO
        # ──────────────────────────────────────────────────────
        "ready_status": "Listo",
        "loading_video_info": "Obteniendo información del vídeo",
        "loading": "⏳ Cargando...",
        "checking_url": "Verificando URL...",
        "download_started": "Descarga iniciada",
        "downloading": "Descargando:",
        "remaining_time": "Tiempo restante:",
        "processing_file": "Procesando archivo...",
        "canceling_download": "Cancelando descarga...",
        "canceling_batch_download": "Cancelando descarga por lotes...",
        "no_file_in_the_queue": "No hay archivos en la cola",

        # ──────────────────────────────────────────────────────
        # LISTAS DE REPRODUCCIÓN
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 Lista de reproducción detectada: {count} vídeo encontrado. Cargando...",
        "playlist_detected_plural": "📋 Lista de reproducción detectada: {count} vídeos encontrados. Cargando...",
        "queue_added_singular": "✅ {count} vídeo añadido a la cola",
        "queue_added_plural": "✅ {count} vídeos añadidos a la cola",

        # ──────────────────────────────────────────────────────
        # MENSAJES DE ÉXITO
        # ──────────────────────────────────────────────────────
        "download_complete": "Descarga completa",
        "download_complete_message": "¡La descarga se completó correctamente!",
        "batch_download_complete": "Descarga por lotes completada",
        "downloads_success_ratio_singular": "✅ {success}/{total} descarga exitosa",
        "downloads_success_ratio_plural": "✅ {success}/{total} descargas exitosas",

        # ──────────────────────────────────────────────────────
        # MENSAJES DE ERROR Y ADVERTENCIA
        # ──────────────────────────────────────────────────────
        "warning": "Advertencia",
        "error": "Error",
        "error_prefix": "Error: ",
        "download_failed": "Error en la descarga",
        "download_canceled": "Descarga cancelada",
        "partial_download_message": "Algunos archivos no se descargaron",
        "enter_valid_url": "Por favor, introduce una URL válida",
        "no_valid_urls": "No se encontraron URLs válidas",
        "no_video": "No se encontró ningún vídeo en esta URL",
        "no_resolutions_found": "No se encontraron resoluciones",
        "no_bitrates_found": "No se encontraron bitrates",
        "fetching_impossible": "No es posible obtener la información del vídeo",
        "playlist_private": "Lista de reproducción privada — inicio de sesión requerido. Proporcione cookies de YouTube.",

        # ──────────────────────────────────────────────────────
        # ARCHIVOS
        # ──────────────────────────────────────────────────────
        "select_output_folder": "Seleccionar carpeta de destino",
        "select_cookies_file": "Seleccionar archivo cookies.txt",
        "load_urls_list": "Cargar lista de URLs",
        "text_files": "Archivos de texto",
        "loaded_urls": "Cargadas {count} URLs desde el archivo",
        "file_load_error": "Error al cargar el archivo: {error}",
        "cannot_read_file": "No se puede leer el archivo: {error}",
        "download_folder": "Descargas",
    },

    # ============================================================
    # 🇮🇹 ITALIANO
    # ============================================================
    "it": {
        # ──────────────────────────────────────────────────────
        # INTESTAZIONE APPLICAZIONE
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "Un downloader multimediale universale con interfaccia grafica basato su yt-dlp",

        # ──────────────────────────────────────────────────────
        # SCHEDE PRINCIPALI
        # ──────────────────────────────────────────────────────
        "single_download_tab": "Download singolo",
        "batch_download_tab": "Download multiplo",
        "tutorial": "Tutorial",

        # ──────────────────────────────────────────────────────
        # PULSANTI E AZIONI
        # ──────────────────────────────────────────────────────
        "check_button": "Aggiungi",
        "download_button": "Scarica",
        "cancel_button": "Annulla",
        "clear_queue": "Svuota coda",
        "browse_button": "Sfoglia",
        "load_from_file_button": "Carica da file",
        "paste_multiple_urls": "Incolla più URL",
        "add_urls": "Aggiungi",

        # ──────────────────────────────────────────────────────
        # CAMPI ED ETICHETTE
        # ──────────────────────────────────────────────────────
        "url_placeholder": "Incolla l'URL di YouTube qui",
        "paste_multiple_urls_hint": "Incolla un URL per riga:",
        "type_label": "Tipo:",
        "video_option": "Video + Audio",
        "audio_only_option": "Solo audio",
        "resolution_label": "Risoluzione:",
        "audio_bitrate_label": "Bitrate audio:",
        "audio_format_label": "Formato audio:",
        "output_folder_label": "Cartella di destinazione:",
        "urls_list_label": "Elenco di URL YouTube (uno per riga):",

        # ──────────────────────────────────────────────────────
        # INFORMAZIONI VIDEO
        # ──────────────────────────────────────────────────────
        "title": "Titolo",
        "author": "Autore",
        "upload_date": "Data di pubblicazione",
        "duration": "Durata",
        "views": "Visualizzazioni",
        "likes": "Mi piace",
        "video_id": "ID video",
        "url": "URL",
        "description": "Descrizione",
        "no_description": "Nessuna descrizione.",
        "available_formats": "Formati disponibili",
        "best_video_format": "Miglior formato solo video: ",
        "best_audio_format": "Miglior formato solo audio: ",

        # ──────────────────────────────────────────────────────
        # POPUP INFO VIDEO
        # ──────────────────────────────────────────────────────
        "video_info_title": "Informazioni sul video",
        "text_summary": "Riepilogo testuale",
        "tab": "Tabella",
        "detailed_summary": "Riepilogo dettagliato",

        # ──────────────────────────────────────────────────────
        # STATO E MESSAGGI DI STATO
        # ──────────────────────────────────────────────────────
        "ready_status": "Pronto",
        "loading_video_info": "Recupero delle informazioni dal video",
        "loading": "⏳ Caricamento...",
        "checking_url": "Verifica dell'URL in corso...",
        "download_started": "Download avviato",
        "downloading": "Scaricamento:",
        "remaining_time": "Tempo rimanente:",
        "processing_file": "Elaborazione file...",
        "canceling_download": "Annullamento del download...",
        "canceling_batch_download": "Annullamento del download multiplo...",
        "no_file_in_the_queue": "Nessun file nella coda",

        # ──────────────────────────────────────────────────────
        # PLAYLIST
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 Playlist rilevata: {count} video trovato. Caricamento...",
        "playlist_detected_plural": "📋 Playlist rilevata: {count} video trovati. Caricamento...",
        "queue_added_singular": "✅ {count} video aggiunto alla coda",
        "queue_added_plural": "✅ {count} video aggiunti alla coda",

        # ──────────────────────────────────────────────────────
        # MESSAGGI DI SUCCESSO
        # ──────────────────────────────────────────────────────
        "download_complete": "Download completato",
        "download_complete_message": "Il download è stato completato con successo!",
        "batch_download_complete": "Download multiplo completato",
        "downloads_success_ratio_singular": "✅ {success}/{total} download riuscito",
        "downloads_success_ratio_plural": "✅ {success}/{total} download riusciti",

        # ──────────────────────────────────────────────────────
        # MESSAGGI DI ERRORE E AVVISO
        # ──────────────────────────────────────────────────────
        "warning": "Attenzione",
        "error": "Errore",
        "error_prefix": "Errore: ",
        "download_failed": "Download fallito",
        "download_canceled": "Download annullato",
        "partial_download_message": "Alcuni file non sono stati scaricati",
        "enter_valid_url": "Inserisci un URL valido",
        "no_valid_urls": "Nessun URL valido trovato",
        "no_video": "Nessun video trovato in questo URL",
        "no_resolutions_found": "Nessuna risoluzione trovata",
        "no_bitrates_found": "Nessun bitrate trovato",
        "fetching_impossible": "Impossibile ottenere le informazioni del video",
        "playlist_private": "Playlist privata — accesso richiesto. Fornire i cookie di YouTube.",

        # ──────────────────────────────────────────────────────
        # FILE
        # ──────────────────────────────────────────────────────
        "select_output_folder": "Seleziona cartella di destinazione",
        "select_cookies_file": "Seleziona file cookies.txt",
        "load_urls_list": "Carica elenco di URL",
        "text_files": "File di testo",
        "loaded_urls": "Caricate {count} URL dal file",
        "file_load_error": "Errore durante il caricamento del file: {error}",
        "cannot_read_file": "Impossibile leggere il file: {error}",
        "download_folder": "Scaricati",
    },

    # ============================================================
    # 🇩🇪 DEUTSCH
    # ============================================================
    "de": {
        # ──────────────────────────────────────────────────────
        # ANWENDUNGS-KOPFZEILE
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "Eine universelle Medien-Downloader-Benutzeroberfläche, die von yt-dlp unterstützt wird",

        # ──────────────────────────────────────────────────────
        # HAUPTREGISTERKARTEN
        # ──────────────────────────────────────────────────────
        "single_download_tab": "Einzeldownload",
        "batch_download_tab": "Stapel-Download",
        "tutorial": "Anleitung",

        # ──────────────────────────────────────────────────────
        # SCHALTFLÄCHEN UND AKTIONEN
        # ──────────────────────────────────────────────────────
        "check_button": "Hinzufügen",
        "download_button": "Herunterladen",
        "cancel_button": "Abbrechen",
        "clear_queue": "Warteschlange leeren",
        "browse_button": "Durchsuchen",
        "load_from_file_button": "Aus Datei laden",
        "paste_multiple_urls": "Mehrere URLs einfügen",
        "add_urls": "Hinzufügen",

        # ──────────────────────────────────────────────────────
        # FELDER UND BESCHRIFTUNGEN
        # ──────────────────────────────────────────────────────
        "url_placeholder": "Füge die YouTube-URL hier ein",
        "paste_multiple_urls_hint": "Füge eine URL pro Zeile ein:",
        "type_label": "Typ:",
        "video_option": "Video + Audio",
        "audio_only_option": "Nur Audio",
        "resolution_label": "Auflösung:",
        "audio_bitrate_label": "Audio-Bitrate:",
        "audio_format_label": "Audio-Format:",
        "output_folder_label": "Zielordner:",
        "urls_list_label": "Liste der YouTube-URLs (eine pro Zeile):",

        # ──────────────────────────────────────────────────────
        # VIDEO-INFORMATIONEN
        # ──────────────────────────────────────────────────────
        "title": "Titel",
        "author": "Autor",
        "upload_date": "Veröffentlichungsdatum",
        "duration": "Dauer",
        "views": "Aufrufe",
        "likes": "Likes",
        "video_id": "Video-ID",
        "url": "URL",
        "description": "Beschreibung",
        "no_description": "Keine Beschreibung.",
        "available_formats": "Verfügbare Formate",
        "best_video_format": "Bestes reines Videoformat: ",
        "best_audio_format": "Bestes reines Audioformat: ",

        # ──────────────────────────────────────────────────────
        # VIDEO-INFO-POPUP
        # ──────────────────────────────────────────────────────
        "video_info_title": "Video-Informationen",
        "text_summary": "Textzusammenfassung",
        "tab": "Tabelle",
        "detailed_summary": "Detaillierte Zusammenfassung",

        # ──────────────────────────────────────────────────────
        # STATUS UND STATUSMELDUNGEN
        # ──────────────────────────────────────────────────────
        "ready_status": "Bereit",
        "loading_video_info": "Video-Informationen werden abgerufen",
        "loading": "⏳ Wird geladen...",
        "checking_url": "URL wird überprüft...",
        "download_started": "Download gestartet",
        "downloading": "Herunterladen:",
        "remaining_time": "Verbleibende Zeit:",
        "processing_file": "Datei wird verarbeitet...",
        "canceling_download": "Download wird abgebrochen...",
        "canceling_batch_download": "Stapel-Download wird abgebrochen...",
        "no_file_in_the_queue": "Keine Datei in der Warteschlange",

        # ──────────────────────────────────────────────────────
        # WIEDERGABELISTEN
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 Wiedergabeliste erkannt: {count} Video gefunden. Wird geladen...",
        "playlist_detected_plural": "📋 Wiedergabeliste erkannt: {count} Videos gefunden. Wird geladen...",
        "queue_added_singular": "✅ {count} Video zur Warteschlange hinzugefügt",
        "queue_added_plural": "✅ {count} Videos zur Warteschlange hinzugefügt",

        # ──────────────────────────────────────────────────────
        # ERFOLGSMELDUNGEN
        # ──────────────────────────────────────────────────────
        "download_complete": "Download abgeschlossen",
        "download_complete_message": "Der Download wurde erfolgreich abgeschlossen!",
        "batch_download_complete": "Stapel-Download abgeschlossen",
        "downloads_success_ratio_singular": "✅ {success}/{total} Download erfolgreich",
        "downloads_success_ratio_plural": "✅ {success}/{total} Downloads erfolgreich",

        # ──────────────────────────────────────────────────────
        # FEHLER- UND WARNMELDUNGEN
        # ──────────────────────────────────────────────────────
        "warning": "Warnung",
        "error": "Fehler",
        "error_prefix": "Fehler: ",
        "download_failed": "Download fehlgeschlagen",
        "download_canceled": "Download abgebrochen",
        "partial_download_message": "Einige Dateien wurden nicht heruntergeladen",
        "enter_valid_url": "Bitte geben Sie eine gültige URL ein",
        "no_valid_urls": "Keine gültigen URLs gefunden",
        "no_video": "Kein Video unter dieser URL gefunden",
        "no_resolutions_found": "Keine Auflösungen gefunden",
        "no_bitrates_found": "Keine Bitraten gefunden",
        "fetching_impossible": "Video-Informationen können nicht abgerufen werden",
        "playlist_private": "Private Wiedergabeliste — Anmeldung erforderlich. Bitte YouTube-Cookies bereitstellen.",

        # ──────────────────────────────────────────────────────
        # DATEIEN
        # ──────────────────────────────────────────────────────
        "select_output_folder": "Zielordner auswählen",
        "select_cookies_file": "cookies.txt-Datei auswählen",
        "load_urls_list": "URL-Liste laden",
        "text_files": "Textdateien",
        "loaded_urls": "{count} URLs aus Datei geladen",
        "file_load_error": "Fehler beim Laden der Datei: {error}",
        "cannot_read_file": "Datei kann nicht gelesen werden: {error}",
        "download_folder": "Downloads",
    },

    # ============================================================
    # 🇵🇹 PORTUGUÊS
    # ============================================================
    "pt": {
        # ──────────────────────────────────────────────────────
        # CABEÇALHO DA APLICAÇÃO
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "Uma GUI universal para download de mídia desenvolvida pela yt-dlp",

        # ──────────────────────────────────────────────────────
        # ABAS PRINCIPAIS
        # ──────────────────────────────────────────────────────
        "single_download_tab": "Download único",
        "batch_download_tab": "Download em lote",
        "tutorial": "Tutorial",

        # ──────────────────────────────────────────────────────
        # BOTÕES E AÇÕES
        # ──────────────────────────────────────────────────────
        "check_button": "Adicionar",
        "download_button": "Baixar",
        "cancel_button": "Cancelar",
        "clear_queue": "Limpar fila",
        "browse_button": "Procurar",
        "load_from_file_button": "Carregar de um arquivo",
        "paste_multiple_urls": "Colar várias URLs",
        "add_urls": "Adicionar",

        # ──────────────────────────────────────────────────────
        # CAMPOS E RÓTULOS
        # ──────────────────────────────────────────────────────
        "url_placeholder": "Cole a URL do YouTube aqui",
        "paste_multiple_urls_hint": "Cole uma URL por linha:",
        "type_label": "Tipo:",
        "video_option": "Vídeo + Áudio",
        "audio_only_option": "Somente áudio",
        "resolution_label": "Resolução:",
        "audio_bitrate_label": "Bitrate de áudio:",
        "audio_format_label": "Formato de áudio:",
        "output_folder_label": "Pasta de destino:",
        "urls_list_label": "Lista de URLs do YouTube (uma por linha):",

        # ──────────────────────────────────────────────────────
        # INFORMAÇÕES DO VÍDEO
        # ──────────────────────────────────────────────────────
        "title": "Título",
        "author": "Autor",
        "upload_date": "Data de envio",
        "duration": "Duração",
        "views": "Visualizações",
        "likes": "Curtidas",
        "video_id": "ID do vídeo",
        "url": "URL",
        "description": "Descrição",
        "no_description": "Sem descrição.",
        "available_formats": "Formatos disponíveis",
        "best_video_format": "Melhor formato somente vídeo:",
        "best_audio_format": "Melhor formato somente áudio:",

        # ──────────────────────────────────────────────────────
        # POPUP DE INFORMAÇÕES DO VÍDEO
        # ──────────────────────────────────────────────────────
        "video_info_title": "Informações do vídeo",
        "text_summary": "Resumo em texto",
        "tab": "Tabela",
        "detailed_summary": "Resumo detalhado",

        # ──────────────────────────────────────────────────────
        # STATUS E MENSAGENS DE ESTADO
        # ──────────────────────────────────────────────────────
        "ready_status": "Pronto",
        "loading_video_info": "Obtendo informações do vídeo",
        "loading": "⏳ Carregando...",
        "checking_url": "Verificando URL...",
        "download_started": "Download iniciado",
        "downloading": "Baixando:",
        "remaining_time": "Tempo restante:",
        "processing_file": "Processando arquivo...",
        "canceling_download": "Cancelando download...",
        "canceling_batch_download": "Cancelando download em lote...",
        "no_file_in_the_queue": "Nenhum arquivo na fila",

        # ──────────────────────────────────────────────────────
        # PLAYLISTS
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 Playlist detectada: {count} vídeo encontrado. Carregando...",
        "playlist_detected_plural": "📋 Playlist detectada: {count} vídeos encontrados. Carregando...",
        "queue_added_singular": "✅ {count} vídeo adicionado à fila",
        "queue_added_plural": "✅ {count} vídeos adicionados à fila",

        # ──────────────────────────────────────────────────────
        # MENSAGENS DE SUCESSO
        # ──────────────────────────────────────────────────────
        "download_complete": "Download concluído",
        "download_complete_message": "O download foi concluído com sucesso!",
        "batch_download_complete": "Download em lote concluído",
        "downloads_success_ratio_singular": "✅ {success}/{total} download concluído",
        "downloads_success_ratio_plural": "✅ {success}/{total} downloads concluídos",

        # ──────────────────────────────────────────────────────
        # MENSAGENS DE ERRO E AVISO
        # ──────────────────────────────────────────────────────
        "warning": "Aviso",
        "error": "Erro",
        "error_prefix": "Erro: ",
        "download_failed": "Falha no download",
        "download_canceled": "Download cancelado",
        "partial_download_message": "Alguns arquivos não foram baixados",
        "enter_valid_url": "Por favor, insira uma URL válida",
        "no_valid_urls": "Nenhuma URL válida encontrada",
        "no_video": "Nenhum vídeo encontrado nesta URL",
        "no_resolutions_found": "Nenhuma resolução encontrada",
        "no_bitrates_found": "Nenhum bitrate encontrado",
        "fetching_impossible": "Não foi possível obter informações do vídeo",
        "playlist_private": "Playlist privada — login necessário. Forneça cookies do YouTube.",

        # ──────────────────────────────────────────────────────
        # ARQUIVOS
        # ──────────────────────────────────────────────────────
        "select_output_folder": "Selecionar pasta de destino",
        "select_cookies_file": "Selecionar arquivo cookies.txt",
        "load_urls_list": "Carregar lista de URLs",
        "text_files": "Arquivos de texto",
        "loaded_urls": "{count} URLs carregadas do arquivo",
        "file_load_error": "Erro ao carregar o arquivo: {error}",
        "cannot_read_file": "Não foi possível ler o arquivo: {error}",
        "download_folder": "Downloads",
    },

    # ============================================================
    # 🇬🇷 ΕΛΛΗΝΙΚΑ
    # ============================================================
    "el": {
        # ──────────────────────────────────────────────────────
        # כותרת היישום
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "Ένα καθολικό GUI για λήψη πολυμέσων που υποστηρίζεται από το yt-dlp",

        # ──────────────────────────────────────────────────────
        # כרטיסיות ראשיות
        # ──────────────────────────────────────────────────────
        "single_download_tab": "Μονή λήψη",
        "batch_download_tab": "Μαζική λήψη",
        "tutorial": "Οδηγός",

        # ──────────────────────────────────────────────────────
        # כפתורים ופעולות
        # ──────────────────────────────────────────────────────
        "check_button": "Προσθήκη",
        "download_button": "Λήψη",
        "cancel_button": "Ακύρωση",
        "clear_queue": "Καθαρισμός ουράς",
        "browse_button": "Αναζήτηση",
        "load_from_file_button": "Φόρτωση από αρχείο",
        "paste_multiple_urls": "Επικόλληση πολλών URL",
        "add_urls": "Προσθήκη",

        # ──────────────────────────────────────────────────────
        # שדות ותוויות
        # ──────────────────────────────────────────────────────
        "url_placeholder": "Επικολλήστε εδώ το URL του YouTube",
        "paste_multiple_urls_hint": "Επικολλήστε ένα URL ανά γραμμή:",
        "type_label": "Τύπος:",
        "video_option": "Βίντεο + Ήχος",
        "audio_only_option": "Μόνο ήχος",
        "resolution_label": "Ανάλυση:",
        "audio_bitrate_label": "Ρυθμός bit ήχου:",
        "audio_format_label": "Μορφή ήχου:",
        "output_folder_label": "Φάκελος εξόδου:",
        "urls_list_label": "Λίστα URL YouTube (ένα ανά γραμμή):",

        # ──────────────────────────────────────────────────────
        # מידע על הווידאו
        # ──────────────────────────────────────────────────────
        "title": "Τίτλος",
        "author": "Δημιουργός",
        "upload_date": "Ημερομηνία ανάρτησης",
        "duration": "Διάρκεια",
        "views": "Προβολές",
        "likes": "Μου αρέσει",
        "video_id": "ID βίντεο",
        "url": "URL",
        "description": "Περιγραφή",
        "no_description": "Δεν υπάρχει περιγραφή.",
        "available_formats": "Διαθέσιμες μορφές",
        "best_video_format": "Καλύτερη μορφή μόνο βίντεο:",
        "best_audio_format": "Καλύτερη μορφή μόνο ήχου:",

        # ──────────────────────────────────────────────────────
        # חלון מידע על הווידאו
        # ──────────────────────────────────────────────────────
        "video_info_title": "Πληροφορίες βίντεο",
        "text_summary": "Κείμενο",
        "tab": "Πίνακας",
        "detailed_summary": "Αναλυτική σύνοψη",

        # ──────────────────────────────────────────────────────
        # מצבים והודעות מצב
        # ──────────────────────────────────────────────────────
        "ready_status": "Έτοιμο",
        "loading_video_info": "Λήψη πληροφοριών βίντεο",
        "loading": "⏳ Φόρτωση...",
        "checking_url": "Έλεγχος URL...",
        "download_started": "Η λήψη ξεκίνησε",
        "downloading": "Λήψη:",
        "remaining_time": "Υπολειπόμενος χρόνος:",
        "processing_file": "Επεξεργασία αρχείου...",
        "canceling_download": "Ακύρωση λήψης...",
        "canceling_batch_download": "Ακύρωση μαζικής λήψης...",
        "no_file_in_the_queue": "Δεν υπάρχουν αρχεία στην ουρά",

        # ──────────────────────────────────────────────────────
        # רשימות השמעה
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 Εντοπίστηκε λίστα αναπαραγωγής: βρέθηκε 1 βίντεο. Φόρτωση...",
        "playlist_detected_plural": "📋 Εντοπίστηκε λίστα αναπαραγωγής: βρέθηκαν {count} βίντεο. Φόρτωση...",
        "queue_added_singular": "✅ Προστέθηκε 1 βίντεο στην ουρά",
        "queue_added_plural": "✅ Προστέθηκαν {count} βίντεο στην ουρά",

        # ──────────────────────────────────────────────────────
        # הודעות הצלחה
        # ──────────────────────────────────────────────────────
        "download_complete": "Η λήψη ολοκληρώθηκε",
        "download_complete_message": "Η λήψη ολοκληρώθηκε με επιτυχία!",
        "batch_download_complete": "Η μαζική λήψη ολοκληρώθηκε",
        "downloads_success_ratio_singular": "✅ Επιτυχής λήψη {success}/{total}",
        "downloads_success_ratio_plural": "✅ Επιτυχείς λήψεις {success}/{total}",

        # ──────────────────────────────────────────────────────
        # הודעות שגיאה ואזהרה
        # ──────────────────────────────────────────────────────
        "warning": "Προειδοποίηση",
        "error": "Σφάλμα",
        "error_prefix": "Σφάλμα: ",
        "download_failed": "Αποτυχία λήψης",
        "download_canceled": "Η λήψη ακυρώθηκε",
        "partial_download_message": "Ορισμένα αρχεία δεν κατέβηκαν",
        "enter_valid_url": "Παρακαλώ εισάγετε έγκυρο URL",
        "no_valid_urls": "Δεν βρέθηκαν έγκυρα URL",
        "no_video": "Δεν βρέθηκε βίντεο για αυτό το URL",
        "no_resolutions_found": "Δεν βρέθηκαν αναλύσεις",
        "no_bitrates_found": "Δεν βρέθηκαν ρυθμοί bit",
        "fetching_impossible": "Αδύνατη η ανάκτηση πληροφοριών βίντεο",
        "playlist_private": "Ιδιωτική λίστα αναπαραγωγής — απαιτείται σύνδεση. Παρέχετε cookies YouTube.",

        # ──────────────────────────────────────────────────────
        # קבצים
        # ──────────────────────────────────────────────────────
        "select_output_folder": "Επιλέξτε φάκελο εξόδου",
        "select_cookies_file": "Επιλέξτε αρχείο cookies.txt",
        "load_urls_list": "Φόρτωση λίστας URL",
        "text_files": "Αρχεία κειμένου",
        "loaded_urls": "Φορτώθηκαν {count} URL από το αρχείο",
        "file_load_error": "Σφάλμα φόρτωσης αρχείου: {error}",
        "cannot_read_file": "Αδυναμία ανάγνωσης αρχείου: {error}",
        "download_folder": "Λήψεις",
    },

    # ============================================================
    # 🇷🇺 РУССКИЙ
    # ============================================================
    "ru": {
        # ──────────────────────────────────────────────────────
        # ЗАГОЛОВОК ПРИЛОЖЕНИЯ
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "Универсальный графический интерфейс для загрузки медиафайлов на базе yt-dlp",

        # ──────────────────────────────────────────────────────
        # ОСНОВНЫЕ ВКЛАДКИ
        # ──────────────────────────────────────────────────────
        "single_download_tab": "Одиночная загрузка",
        "batch_download_tab": "Пакетная загрузка",
        "tutorial": "Руководство",

        # ──────────────────────────────────────────────────────
        # КНОПКИ И ДЕЙСТВИЯ
        # ──────────────────────────────────────────────────────
        "check_button": "Добавить",
        "download_button": "Скачать",
        "cancel_button": "Отмена",
        "clear_queue": "Очистить очередь",
        "browse_button": "Обзор",
        "load_from_file_button": "Загрузить из файла",
        "paste_multiple_urls": "Вставить несколько URL",
        "add_urls": "Добавить",

        # ──────────────────────────────────────────────────────
        # ПОЛЯ И МЕТКИ
        # ──────────────────────────────────────────────────────
        "url_placeholder": "Вставьте URL YouTube здесь",
        "paste_multiple_urls_hint": "Вставьте по одному URL на строку:",
        "type_label": "Тип:",
        "video_option": "Видео + Аудио",
        "audio_only_option": "Только аудио",
        "resolution_label": "Разрешение:",
        "audio_bitrate_label": "Аудио битрейт:",
        "audio_format_label": "Аудио формат:",
        "output_folder_label": "Папка вывода:",
        "urls_list_label": "Список URL YouTube (по одному на строку):",

        # ──────────────────────────────────────────────────────
        # ИНФОРМАЦИЯ О ВИДЕО
        # ──────────────────────────────────────────────────────
        "title": "Название",
        "author": "Автор",
        "upload_date": "Дата публикации",
        "duration": "Длительность",
        "views": "Просмотры",
        "likes": "Лайки",
        "video_id": "ID видео",
        "url": "URL",
        "description": "Описание",
        "no_description": "Описание отсутствует.",
        "available_formats": "Доступные форматы",
        "best_video_format": "Лучший формат только видео:",
        "best_audio_format": "Лучший формат только аудио:",

        # ──────────────────────────────────────────────────────
        # ВСПЛЫВАЮЩЕЕ ОКНО ИНФОРМАЦИИ О ВИДЕО
        # ──────────────────────────────────────────────────────
        "video_info_title": "Информация о видео",
        "text_summary": "Текстовое резюме",
        "tab": "Таблица",
        "detailed_summary": "Подробное резюме",

        # ──────────────────────────────────────────────────────
        # СТАТУСЫ И СООБЩЕНИЯ СОСТОЯНИЯ
        # ──────────────────────────────────────────────────────
        "ready_status": "Готово",
        "loading_video_info": "Получение информации о видео",
        "loading": "⏳ Загрузка...",
        "checking_url": "Проверка URL...",
        "download_started": "Загрузка началась",
        "downloading": "Загрузка:",
        "remaining_time": "Оставшееся время:",
        "processing_file": "Обработка файла...",
        "canceling_download": "Отмена загрузки...",
        "canceling_batch_download": "Отмена пакетной загрузки...",
        "no_file_in_the_queue": "Очередь пуста",

        # ──────────────────────────────────────────────────────
        # ПЛЕЙЛИСТЫ
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 Обнаружен плейлист: найдено {count} видео. Загрузка...",
        "playlist_detected_plural": "📋 Обнаружен плейлист: найдено {count} видео. Загрузка...",
        "queue_added_singular": "✅ {count} видео добавлено в очередь",
        "queue_added_plural": "✅ {count} видео добавлены в очередь",

        # ──────────────────────────────────────────────────────
        # СООБЩЕНИЯ ОБ УСПЕХЕ
        # ──────────────────────────────────────────────────────
        "download_complete": "Загрузка завершена",
        "download_complete_message": "Загрузка успешно завершена!",
        "batch_download_complete": "Пакетная загрузка завершена",
        "downloads_success_ratio_singular": "✅ {success}/{total} загрузка успешна",
        "downloads_success_ratio_plural": "✅ {success}/{total} загрузок успешно",

        # ──────────────────────────────────────────────────────
        # СООБЩЕНИЯ ОБ ОШИБКАХ И ПРЕДУПРЕЖДЕНИЯ
        # ──────────────────────────────────────────────────────
        "warning": "Предупреждение",
        "error": "Ошибка",
        "error_prefix": "Ошибка: ",
        "download_failed": "Ошибка загрузки",
        "download_canceled": "Загрузка отменена",
        "partial_download_message": "Некоторые файлы не были загружены",
        "enter_valid_url": "Пожалуйста, введите корректный URL",
        "no_valid_urls": "Корректные URL не найдены",
        "no_video": "Видео по этому URL не найдено",
        "no_resolutions_found": "Разрешения не найдены",
        "no_bitrates_found": "Битрейты не найдены",
        "fetching_impossible": "Невозможно получить информацию о видео",
        "playlist_private": "Приватный плейлист — требуется вход. Укажите cookies YouTube.",

        # ──────────────────────────────────────────────────────
        # ФАЙЛЫ
        # ──────────────────────────────────────────────────────
        "select_output_folder": "Выбрать папку назначения",
        "select_cookies_file": "Выбрать файл cookies.txt",
        "load_urls_list": "Загрузить список URL",
        "text_files": "Текстовые файлы",
        "loaded_urls": "Загружено {count} URL из файла",
        "file_load_error": "Ошибка загрузки файла: {error}",
        "cannot_read_file": "Невозможно прочитать файл: {error}",
        "download_folder": "Загрузки",
    },

    # ============================================================
    # 🇯🇵 日本語
    # ============================================================
    "ja": {
        # ──────────────────────────────────────────────────────
        # アプリケーションヘッダー
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "yt-dlpを基盤としたユニバーサルメディアダウンローダーGUI",

        # ──────────────────────────────────────────────────────
        # メインタブ
        # ──────────────────────────────────────────────────────
        "single_download_tab": "単一ダウンロード",
        "batch_download_tab": "一括ダウンロード",
        "tutorial": "チュートリアル",

        # ──────────────────────────────────────────────────────
        # ボタンと操作
        # ──────────────────────────────────────────────────────
        "check_button": "追加",
        "download_button": "ダウンロード",
        "cancel_button": "キャンセル",
        "clear_queue": "キューを空にする",
        "browse_button": "参照",
        "load_from_file_button": "ファイルから読み込む",
        "paste_multiple_urls": "複数のURLを貼り付け",
        "add_urls": "追加",

        # ──────────────────────────────────────────────────────
        # フィールドとラベル
        # ──────────────────────────────────────────────────────
        "url_placeholder": "ここにYouTubeのURLを貼り付けてください",
        "paste_multiple_urls_hint": "1行に1つのURLを貼り付けてください：",
        "type_label": "タイプ：",
        "video_option": "動画 + 音声",
        "audio_only_option": "音声のみ",
        "resolution_label": "解像度：",
        "audio_bitrate_label": "音声ビットレート：",
        "audio_format_label": "音声フォーマット：",
        "output_folder_label": "出力フォルダ：",
        "urls_list_label": "YouTube URL一覧（1行に1つ）：",

        # ──────────────────────────────────────────────────────
        # 動画情報
        # ──────────────────────────────────────────────────────
        "title": "タイトル",
        "author": "投稿者",
        "upload_date": "公開日",
        "duration": "再生時間",
        "views": "再生回数",
        "likes": "高評価",
        "video_id": "動画ID",
        "url": "URL",
        "description": "説明",
        "no_description": "説明はありません。",
        "available_formats": "利用可能なフォーマット",
        "best_video_format": "最適な動画のみの形式：",
        "best_audio_format": "最適な音声のみの形式：",

        # ──────────────────────────────────────────────────────
        # 動画情報ポップアップ
        # ──────────────────────────────────────────────────────
        "video_info_title": "動画情報",
        "text_summary": "テキスト要約",
        "tab": "表",
        "detailed_summary": "詳細な要約",

        # ──────────────────────────────────────────────────────
        # ステータスと状態メッセージ
        # ──────────────────────────────────────────────────────
        "ready_status": "準備完了",
        "loading_video_info": "動画情報を取得中",
        "loading": "⏳ 読み込み中...",
        "checking_url": "URLを確認中...",
        "download_started": "ダウンロード開始",
        "downloading": "ダウンロード中：",
        "remaining_time": "残り時間：",
        "processing_file": "ファイル処理中...",
        "canceling_download": "ダウンロードをキャンセル中...",
        "canceling_batch_download": "一括ダウンロードをキャンセル中...",
        "no_file_in_the_queue": "キューにファイルがありません",

        # ──────────────────────────────────────────────────────
        # プレイリスト
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 プレイリスト検出：{count} 件の動画が見つかりました。読み込み中...",
        "playlist_detected_plural": "📋 プレイリスト検出：{count} 件の動画が見つかりました。読み込み中...",
        "queue_added_singular": "✅ {count} 件の動画をキューに追加しました",
        "queue_added_plural": "✅ {count} 件の動画をキューに追加しました",

        # ──────────────────────────────────────────────────────
        # 成功メッセージ
        # ──────────────────────────────────────────────────────
        "download_complete": "ダウンロード完了",
        "download_complete_message": "ダウンロードが正常に完了しました！",
        "batch_download_complete": "一括ダウンロード完了",
        "downloads_success_ratio_singular": "✅ {success}/{total} 件のダウンロード成功",
        "downloads_success_ratio_plural": "✅ {success}/{total} 件のダウンロード成功",

        # ──────────────────────────────────────────────────────
        # エラーおよび警告メッセージ
        # ──────────────────────────────────────────────────────
        "warning": "警告",
        "error": "エラー",
        "error_prefix": "エラー：",
        "download_failed": "ダウンロード失敗",
        "download_canceled": "ダウンロードがキャンセルされました",
        "partial_download_message": "一部のファイルがダウンロードされませんでした",
        "enter_valid_url": "有効なURLを入力してください",
        "no_valid_urls": "有効なURLが見つかりません",
        "no_video": "このURLには動画が見つかりません",
        "no_resolutions_found": "解像度が見つかりません",
        "no_bitrates_found": "ビットレートが見つかりません",
        "fetching_impossible": "動画情報を取得できません",
        "playlist_private": "非公開プレイリスト — ログインが必要です。YouTubeのCookieを指定してください。",

        # ──────────────────────────────────────────────────────
        # ファイル
        # ──────────────────────────────────────────────────────
        "select_output_folder": "出力フォルダを選択",
        "select_cookies_file": "cookies.txt ファイルを選択",
        "load_urls_list": "URLリストを読み込む",
        "text_files": "テキストファイル",
        "loaded_urls": "ファイルから {count} 件のURLを読み込みました",
        "file_load_error": "ファイル読み込みエラー：{error}",
        "cannot_read_file": "ファイルを読み取れません：{error}",
        "download_folder": "ダウンロード",
    },

    # ============================================================
    # 🇨🇳 中文（简体）
    # ============================================================
    "zh": {
        # ──────────────────────────────────────────────────────
        # 应用程序标题
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "基于yt-dlp的通用媒体下载器图形界面",

        # ──────────────────────────────────────────────────────
        # 主选项卡
        # ──────────────────────────────────────────────────────
        "single_download_tab": "单个下载",
        "batch_download_tab": "批量下载",
        "tutorial": "教程",

        # ──────────────────────────────────────────────────────
        # 按钮和操作
        # ──────────────────────────────────────────────────────
        "check_button": "添加",
        "download_button": "下载",
        "cancel_button": "取消",
        "clear_queue": "清空队列",
        "browse_button": "浏览",
        "load_from_file_button": "从文件加载",
        "paste_multiple_urls": "粘贴多个URL",
        "add_urls": "添加",

        # ──────────────────────────────────────────────────────
        # 字段和标签
        # ──────────────────────────────────────────────────────
        "url_placeholder": "在此粘贴 YouTube URL",
        "paste_multiple_urls_hint": "每行粘贴一个 URL：",
        "type_label": "类型：",
        "video_option": "视频 + 音频",
        "audio_only_option": "仅音频",
        "resolution_label": "分辨率：",
        "audio_bitrate_label": "音频比特率：",
        "audio_format_label": "音频格式：",
        "output_folder_label": "输出文件夹：",
        "urls_list_label": "YouTube URL 列表（每行一个）：",

        # ──────────────────────────────────────────────────────
        # 视频信息
        # ──────────────────────────────────────────────────────
        "title": "标题",
        "author": "作者",
        "upload_date": "上传日期",
        "duration": "时长",
        "views": "观看次数",
        "likes": "点赞",
        "video_id": "视频ID",
        "url": "URL",
        "description": "描述",
        "no_description": "无描述。",
        "available_formats": "可用格式",
        "best_video_format": "最佳纯视频格式：",
        "best_audio_format": "最佳纯音频格式：",

        # ──────────────────────────────────────────────────────
        # 视频信息弹窗
        # ──────────────────────────────────────────────────────
        "video_info_title": "视频信息",
        "text_summary": "文本摘要",
        "tab": "表格",
        "detailed_summary": "详细摘要",

        # ──────────────────────────────────────────────────────
        # 状态和状态消息
        # ──────────────────────────────────────────────────────
        "ready_status": "就绪",
        "loading_video_info": "正在获取视频信息",
        "loading": "⏳ 加载中...",
        "checking_url": "正在检查 URL...",
        "download_started": "下载已开始",
        "downloading": "下载中：",
        "remaining_time": "剩余时间：",
        "processing_file": "正在处理文件...",
        "canceling_download": "正在取消下载...",
        "canceling_batch_download": "正在取消批量下载...",
        "no_file_in_the_queue": "队列中没有文件",

        # ──────────────────────────────────────────────────────
        # 播放列表
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 检测到播放列表：找到 {count} 个视频，正在加载...",
        "playlist_detected_plural": "📋 检测到播放列表：找到 {count} 个视频，正在加载...",
        "queue_added_singular": "✅ 已添加 {count} 个视频到队列",
        "queue_added_plural": "✅ 已添加 {count} 个视频到队列",

        # ──────────────────────────────────────────────────────
        # 成功消息
        # ──────────────────────────────────────────────────────
        "download_complete": "下载完成",
        "download_complete_message": "下载已成功完成！",
        "batch_download_complete": "批量下载完成",
        "downloads_success_ratio_singular": "✅ 成功下载 {success}/{total} 个文件",
        "downloads_success_ratio_plural": "✅ 成功下载 {success}/{total} 个文件",

        # ──────────────────────────────────────────────────────
        # 错误和警告消息
        # ──────────────────────────────────────────────────────
        "warning": "警告",
        "error": "错误",
        "error_prefix": "错误：",
        "download_failed": "下载失败",
        "download_canceled": "下载已取消",
        "partial_download_message": "部分文件未能下载",
        "enter_valid_url": "请输入有效的 URL",
        "no_valid_urls": "未找到有效的 URL",
        "no_video": "该 URL 未找到视频",
        "no_resolutions_found": "未找到分辨率",
        "no_bitrates_found": "未找到比特率",
        "fetching_impossible": "无法获取视频信息",
        "playlist_private": "私有播放列表 — 需要登录。请提供 YouTube Cookies。",

        # ──────────────────────────────────────────────────────
        # 文件
        # ──────────────────────────────────────────────────────
        "select_output_folder": "选择输出文件夹",
        "select_cookies_file": "选择 cookies.txt 文件",
        "load_urls_list": "加载 URL 列表",
        "text_files": "文本文件",
        "loaded_urls": "已从文件加载 {count} 个 URL",
        "file_load_error": "文件加载错误：{error}",
        "cannot_read_file": "无法读取文件：{error}",
        "download_folder": "下载",
    },

    # ============================================================
    # 🇰🇷 한국어
    # ============================================================
    "ko": {
        # ──────────────────────────────────────────────────────
        # 애플리케이션 헤더
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "yt-dlp 기반의 범용 미디어 다운로더 GUI",

        # ──────────────────────────────────────────────────────
        # 기본 탭
        # ──────────────────────────────────────────────────────
        "single_download_tab": "단일 다운로드",
        "batch_download_tab": "일괄 다운로드",
        "tutorial": "튜토리얼",

        # ──────────────────────────────────────────────────────
        # 버튼 및 동작
        # ──────────────────────────────────────────────────────
        "check_button": "추가",
        "download_button": "다운로드",
        "cancel_button": "취소",
        "clear_queue": "대기열 비우기",
        "browse_button": "찾아보기",
        "load_from_file_button": "파일에서 불러오기",
        "paste_multiple_urls": "여러 URL 붙여넣기",
        "add_urls": "추가",

        # ──────────────────────────────────────────────────────
        # 필드 및 레이블
        # ──────────────────────────────────────────────────────
        "url_placeholder": "여기에 YouTube URL을 붙여넣으세요",
        "paste_multiple_urls_hint": "한 줄에 하나의 URL을 붙여넣으세요:",
        "type_label": "유형:",
        "video_option": "비디오 + 오디오",
        "audio_only_option": "오디오만",
        "resolution_label": "해상도:",
        "audio_bitrate_label": "오디오 비트레이트:",
        "audio_format_label": "오디오 형식:",
        "output_folder_label": "출력 폴더:",
        "urls_list_label": "YouTube URL 목록 (한 줄에 하나):",

        # ──────────────────────────────────────────────────────
        # 비디오 정보
        # ──────────────────────────────────────────────────────
        "title": "제목",
        "author": "작성자",
        "upload_date": "업로드 날짜",
        "duration": "길이",
        "views": "조회수",
        "likes": "좋아요",
        "video_id": "비디오 ID",
        "url": "URL",
        "description": "설명",
        "no_description": "설명 없음.",
        "available_formats": "사용 가능한 형식",
        "best_video_format": "최고의 비디오 전용 형식:",
        "best_audio_format": "최고의 오디오 전용 형식:",

        # ──────────────────────────────────────────────────────
        # 비디오 정보 팝업
        # ──────────────────────────────────────────────────────
        "video_info_title": "비디오 정보",
        "text_summary": "텍스트 요약",
        "tab": "표",
        "detailed_summary": "상세 요약",

        # ──────────────────────────────────────────────────────
        # 상태 및 상태 메시지
        # ──────────────────────────────────────────────────────
        "ready_status": "준비 완료",
        "loading_video_info": "비디오 정보 불러오는 중",
        "loading": "⏳ 로딩 중...",
        "checking_url": "URL 확인 중...",
        "download_started": "다운로드 시작됨",
        "downloading": "다운로드 중:",
        "remaining_time": "남은 시간:",
        "processing_file": "파일 처리 중...",
        "canceling_download": "다운로드 취소 중...",
        "canceling_batch_download": "일괄 다운로드 취소 중...",
        "no_file_in_the_queue": "대기열에 파일이 없습니다",

        # ──────────────────────────────────────────────────────
        # 재생목록
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 재생목록 감지됨: {count}개 비디오 발견. 로딩 중...",
        "playlist_detected_plural": "📋 재생목록 감지됨: {count}개 비디오 발견. 로딩 중...",
        "queue_added_singular": "✅ {count}개 비디오가 대기열에 추가됨",
        "queue_added_plural": "✅ {count}개 비디오가 대기열에 추가됨",

        # ──────────────────────────────────────────────────────
        # 성공 메시지
        # ──────────────────────────────────────────────────────
        "download_complete": "다운로드 완료",
        "download_complete_message": "다운로드가 성공적으로 완료되었습니다!",
        "batch_download_complete": "일괄 다운로드 완료",
        "downloads_success_ratio_singular": "✅ {success}/{total} 다운로드 성공",
        "downloads_success_ratio_plural": "✅ {success}/{total} 다운로드 성공",

        # ──────────────────────────────────────────────────────
        # 오류 및 경고 메시지
        # ──────────────────────────────────────────────────────
        "warning": "경고",
        "error": "오류",
        "error_prefix": "오류: ",
        "download_failed": "다운로드 실패",
        "download_canceled": "다운로드 취소됨",
        "partial_download_message": "일부 파일이 다운로드되지 않았습니다",
        "enter_valid_url": "유효한 URL을 입력하세요",
        "no_valid_urls": "유효한 URL이 없습니다",
        "no_video": "이 URL에서 비디오를 찾을 수 없습니다",
        "no_resolutions_found": "해상도를 찾을 수 없습니다",
        "no_bitrates_found": "비트레이트를 찾을 수 없습니다",
        "fetching_impossible": "비디오 정보를 가져올 수 없습니다",
        "playlist_private": "비공개 재생목록 — 로그인 필요. YouTube 쿠키를 제공하세요.",

        # ──────────────────────────────────────────────────────
        # 파일
        # ──────────────────────────────────────────────────────
        "select_output_folder": "출력 폴더 선택",
        "select_cookies_file": "cookies.txt 파일 선택",
        "load_urls_list": "URL 목록 불러오기",
        "text_files": "텍스트 파일",
        "loaded_urls": "파일에서 {count}개의 URL을 불러왔습니다",
        "file_load_error": "파일 불러오기 오류: {error}",
        "cannot_read_file": "파일을 읽을 수 없습니다: {error}",
        "download_folder": "다운로드",
    },

    # ============================================================
    # 🇵🇱 POLSKI
    # ============================================================
    "pl": {
        # ──────────────────────────────────────────────────────
        # NAGŁÓWEK APLIKACJI
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "Uniwersalny interfejs graficzny do pobierania multimediów oparty na yt-dlp",

        # ──────────────────────────────────────────────────────
        # GŁÓWNE ZAKŁADKI
        # ──────────────────────────────────────────────────────
        "single_download_tab": "Pobieranie pojedyncze",
        "batch_download_tab": "Pobieranie wsadowe",
        "tutorial": "Samouczek",

        # ──────────────────────────────────────────────────────
        # PRZYCISKI I AKCJE
        # ──────────────────────────────────────────────────────
        "check_button": "Dodaj",
        "download_button": "Pobierz",
        "cancel_button": "Anuluj",
        "clear_queue": "Wyczyść kolejkę",
        "browse_button": "Przeglądaj",
        "load_from_file_button": "Wczytaj z pliku",
        "paste_multiple_urls": "Wklej wiele URL",
        "add_urls": "Dodaj",

        # ──────────────────────────────────────────────────────
        # POLA I ETYKIETY
        # ──────────────────────────────────────────────────────
        "url_placeholder": "Wklej tutaj URL YouTube",
        "paste_multiple_urls_hint": "Wklej jeden URL na linię:",
        "type_label": "Typ:",
        "video_option": "Wideo + Audio",
        "audio_only_option": "Tylko audio",
        "resolution_label": "Rozdzielczość:",
        "audio_bitrate_label": "Bitrate audio:",
        "audio_format_label": "Format audio:",
        "output_folder_label": "Folder wyjściowy:",
        "urls_list_label": "Lista URL YouTube (jeden na linię):",

        # ──────────────────────────────────────────────────────
        # INFORMACJE O WIDEO
        # ──────────────────────────────────────────────────────
        "title": "Tytuł",
        "author": "Autor",
        "upload_date": "Data publikacji",
        "duration": "Czas trwania",
        "views": "Wyświetlenia",
        "likes": "Polubienia",
        "video_id": "ID wideo",
        "url": "URL",
        "description": "Opis",
        "no_description": "Brak opisu.",
        "available_formats": "Dostępne formaty",
        "best_video_format": "Najlepszy format tylko wideo:",
        "best_audio_format": "Najlepszy format tylko audio:",

        # ──────────────────────────────────────────────────────
        # OKNO INFORMACJI O WIDEO
        # ──────────────────────────────────────────────────────
        "video_info_title": "Informacje o wideo",
        "text_summary": "Podsumowanie tekstowe",
        "tab": "Tabela",
        "detailed_summary": "Szczegółowe podsumowanie",

        # ──────────────────────────────────────────────────────
        # STATUSY I KOMUNIKATY STANU
        # ──────────────────────────────────────────────────────
        "ready_status": "Gotowe",
        "loading_video_info": "Pobieranie informacji o wideo",
        "loading": "⏳ Ładowanie...",
        "checking_url": "Sprawdzanie URL...",
        "download_started": "Pobieranie rozpoczęte",
        "downloading": "Pobieranie:",
        "remaining_time": "Pozostały czas:",
        "processing_file": "Przetwarzanie pliku...",
        "canceling_download": "Anulowanie pobierania...",
        "canceling_batch_download": "Anulowanie pobierania wsadowego...",
        "no_file_in_the_queue": "Brak plików w kolejce",

        # ──────────────────────────────────────────────────────
        # PLAYLISTY
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 Wykryto playlistę: znaleziono {count} wideo. Ładowanie...",
        "playlist_detected_plural": "📋 Wykryto playlistę: znaleziono {count} wideo. Ładowanie...",
        "queue_added_singular": "✅ {count} wideo dodane do kolejki",
        "queue_added_plural": "✅ {count} wideo dodane do kolejki",

        # ──────────────────────────────────────────────────────
        # KOMUNIKATY SUKCESU
        # ──────────────────────────────────────────────────────
        "download_complete": "Pobieranie zakończone",
        "download_complete_message": "Pobieranie zakończone sukcesem!",
        "batch_download_complete": "Pobieranie wsadowe zakończone",
        "downloads_success_ratio_singular": "✅ {success}/{total} pobieranie zakończone",
        "downloads_success_ratio_plural": "✅ {success}/{total} pobrań zakończonych",

        # ──────────────────────────────────────────────────────
        # KOMUNIKATY BŁĘDÓW I OSTRZEŻENIA
        # ──────────────────────────────────────────────────────
        "warning": "Ostrzeżenie",
        "error": "Błąd",
        "error_prefix": "Błąd: ",
        "download_failed": "Błąd pobierania",
        "download_canceled": "Pobieranie anulowane",
        "partial_download_message": "Niektóre pliki nie zostały pobrane",
        "enter_valid_url": "Wprowadź poprawny URL",
        "no_valid_urls": "Nie znaleziono poprawnych URL",
        "no_video": "Nie znaleziono wideo dla tego URL",
        "no_resolutions_found": "Nie znaleziono rozdzielczości",
        "no_bitrates_found": "Nie znaleziono bitrate",
        "fetching_impossible": "Nie można pobrać informacji o wideo",
        "playlist_private": "Prywatna playlista — wymagane logowanie. Podaj plik cookies YouTube.",

        # ──────────────────────────────────────────────────────
        # PLIKI
        # ──────────────────────────────────────────────────────
        "select_output_folder": "Wybierz folder wyjściowy",
        "select_cookies_file": "Wybierz plik cookies.txt",
        "load_urls_list": "Wczytaj listę URL",
        "text_files": "Pliki tekstowe",
        "loaded_urls": "Wczytano {count} URL z pliku",
        "file_load_error": "Błąd wczytywania pliku: {error}",
        "cannot_read_file": "Nie można odczytać pliku: {error}",
        "download_folder": "Pobrane",
    },

    # ============================================================
    # 🇮🇱 עברית
    # ============================================================
    "he": {
        # ──────────────────────────────────────────────────────
        # ΚΕΦΑΛΙΔΑ ΕΦΑΡΜΟΓΗΣ
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "ממשק משתמש גרפי להורדת מדיה אוניברסלי המופעל על ידי yt-dlp",

        # ──────────────────────────────────────────────────────
        # ΚΥΡΙΕΣ ΚΑΡΤΕΛΕΣ
        # ──────────────────────────────────────────────────────
        "single_download_tab": "הורדה בודדת",
        "batch_download_tab": "הורדה מרובה",
        "tutorial": "מדריך",

        # ──────────────────────────────────────────────────────
        # ΚΟΥΜΠΙΑ ΚΑΙ ΕΝΕΡΓΕΙΕΣ
        # ──────────────────────────────────────────────────────
        "check_button": "הוספה",
        "download_button": "הורדה",
        "cancel_button": "ביטול",
        "clear_queue": "ניקוי התור",
        "browse_button": "עיון",
        "load_from_file_button": "טעינה מקובץ",
        "paste_multiple_urls": "הדבקת מספר כתובות",
        "add_urls": "הוספה",

        # ──────────────────────────────────────────────────────
        # ΠΕΔΙΑ ΚΑΙ ΕΤΙΚΕΤΕΣ
        # ──────────────────────────────────────────────────────
        "url_placeholder": "הדבק כאן כתובת YouTube",
        "paste_multiple_urls_hint": "הדבק כתובת אחת בכל שורה:",
        "type_label": "סוג:",
        "video_option": "וידאו + שמע",
        "audio_only_option": "שמע בלבד",
        "resolution_label": "רזולוציה:",
        "audio_bitrate_label": "קצב סיביות שמע:",
        "audio_format_label": "פורמט שמע:",
        "output_folder_label": "תיקיית יעד:",
        "urls_list_label": "רשימת כתובות YouTube (אחת בכל שורה):",

        # ──────────────────────────────────────────────────────
        # ΠΛΗΡΟΦΟΡΙΕΣ ΒΙΝΤΕΟ
        # ──────────────────────────────────────────────────────
        "title": "כותרת",
        "author": "יוצר",
        "upload_date": "תאריך העלאה",
        "duration": "משך",
        "views": "צפיות",
        "likes": "לייקים",
        "video_id": "מזהה וידאו",
        "url": "כתובת",
        "description": "תיאור",
        "no_description": "אין תיאור.",
        "available_formats": "פורמטים זמינים",
        "best_video_format": "פורמט הווידאו הטוב ביותר בלבד:",
        "best_audio_format": "פורמט השמע הטוב ביותר בלבד:",

        # ──────────────────────────────────────────────────────
        # ΠΑΡΑΘΥΡΟ ΠΛΗΡΟΦΟΡΙΩΝ ΒΙΝΤΕΟ
        # ──────────────────────────────────────────────────────
        "video_info_title": "מידע על הווידאו",
        "text_summary": "סיכום טקסט",
        "tab": "טבלה",
        "detailed_summary": "סיכום מפורט",

        # ──────────────────────────────────────────────────────
        # ΚΑΤΑΣΤΑΣΕΙΣ ΚΑΙ ΜΗΝΥΜΑΤΑ ΚΑΤΑΣΤΑΣΗΣ
        # ──────────────────────────────────────────────────────
        "ready_status": "מוכן",
        "loading_video_info": "איסוף מידע על הווידאו",
        "loading": "⏳ טוען...",
        "checking_url": "בודק כתובת...",
        "download_started": "ההורדה החלה",
        "downloading": "מוריד:",
        "remaining_time": "זמן נותר:",
        "processing_file": "מעבד קובץ...",
        "canceling_download": "מבטל הורדה...",
        "canceling_batch_download": "מבטל הורדה מרובה...",
        "no_file_in_the_queue": "אין קבצים בתור",

        # ──────────────────────────────────────────────────────
        # ΛΙΣΤΕΣ ΑΝΑΠΑΡΑΓΩΓΗΣ
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 זוהתה רשימת השמעה: נמצא וידאו אחד. טוען...",
        "playlist_detected_plural": "📋 זוהתה רשימת השמעה: נמצאו {count} סרטונים. טוען...",
        "queue_added_singular": "✅ וידאו אחד נוסף לתור",
        "queue_added_plural": "✅ {count} סרטונים נוספו לתור",

        # ──────────────────────────────────────────────────────
        # ΜΗΝΥΜΑΤΑ ΕΠΙΤΥΧΙΑΣ
        # ──────────────────────────────────────────────────────
        "download_complete": "ההורדה הושלמה",
        "download_complete_message": "ההורדה הושלמה בהצלחה!",
        "batch_download_complete": "הורדה מרובה הושלמה",
        "downloads_success_ratio_singular": "✅ הורדה מוצלחת {success}/{total}",
        "downloads_success_ratio_plural": "✅ הורדות מוצלחות {success}/{total}",

        # ──────────────────────────────────────────────────────
        # ΜΗΝΥΜΑΤΑ ΣΦΑΛΜΑΤΩΝ ΚΑΙ ΠΡΟΕΙΔΟΠΟΙΗΣΕΩΝ
        # ──────────────────────────────────────────────────────
        "warning": "אזהרה",
        "error": "שגיאה",
        "error_prefix": "שגיאה: ",
        "download_failed": "ההורדה נכשלה",
        "download_canceled": "ההורדה בוטלה",
        "partial_download_message": "חלק מהקבצים לא הורדו",
        "enter_valid_url": "אנא הזן כתובת תקינה",
        "no_valid_urls": "לא נמצאו כתובות תקינות",
        "no_video": "לא נמצא וידאו עבור כתובת זו",
        "no_resolutions_found": "לא נמצאו רזולוציות",
        "no_bitrates_found": "לא נמצאו קצבי סיביות",
        "fetching_impossible": "לא ניתן לאחזר את מידע הווידאו",
        "playlist_private": "רשימת השמעה פרטית — נדרשת התחברות. אנא ספק קובצי cookies של YouTube.",

        # ──────────────────────────────────────────────────────
        # ΑΡΧΕΙΑ
        # ──────────────────────────────────────────────────────
        "select_output_folder": "בחר תיקיית יעד",
        "select_cookies_file": "בחר קובץ cookies.txt",
        "load_urls_list": "טעינת רשימת כתובות",
        "text_files": "קובצי טקסט",
        "loaded_urls": "נטענו {count} כתובות מהקובץ",
        "file_load_error": "שגיאה בטעינת הקובץ: {error}",
        "cannot_read_file": "לא ניתן לקרוא את הקובץ: {error}",
        "download_folder": "הורדות",
    },

    # ============================================================
    # 🇸🇦 العربية
    # ============================================================
    "ar": {
        # ──────────────────────────────────────────────────────
        # رأس التطبيق
        # ──────────────────────────────────────────────────────
        "app_title": "GOD",
        "acronym": "God Offers Downloads, Graphical Omnipotent Downloader",
        "app_subtitle": "واجهة مستخدم رسومية عالمية لتنزيل الوسائط مدعومة بواسطة yt-dlp",

        # ──────────────────────────────────────────────────────
        # علامات التبويب الرئيسية
        # ──────────────────────────────────────────────────────
        "single_download_tab": "تنزيل فردي",
        "batch_download_tab": "تنزيل جماعي",
        "tutorial": "دليل الاستخدام",

        # ──────────────────────────────────────────────────────
        # الأزرار والإجراءات
        # ──────────────────────────────────────────────────────
        "check_button": "إضافة",
        "download_button": "تنزيل",
        "cancel_button": "إلغاء",
        "clear_queue": "تفريغ قائمة الانتظار",
        "browse_button": "استعراض",
        "load_from_file_button": "تحميل من ملف",
        "paste_multiple_urls": "لصق عدة روابط",
        "add_urls": "إضافة",

        # ──────────────────────────────────────────────────────
        # الحقول والتسميات
        # ──────────────────────────────────────────────────────
        "url_placeholder": "الصق رابط YouTube هنا",
        "paste_multiple_urls_hint": "الصق رابطًا واحدًا في كل سطر:",
        "type_label": "النوع:",
        "video_option": "فيديو + صوت",
        "audio_only_option": "صوت فقط",
        "resolution_label": "الدقة:",
        "audio_bitrate_label": "معدل البت الصوتي:",
        "audio_format_label": "تنسيق الصوت:",
        "output_folder_label": "مجلد الإخراج:",
        "urls_list_label": "قائمة روابط YouTube (رابط واحد لكل سطر):",

        # ──────────────────────────────────────────────────────
        # معلومات الفيديو
        # ──────────────────────────────────────────────────────
        "title": "العنوان",
        "author": "الناشر",
        "upload_date": "تاريخ النشر",
        "duration": "المدة",
        "views": "المشاهدات",
        "likes": "الإعجابات",
        "video_id": "معرّف الفيديو",
        "url": "الرابط",
        "description": "الوصف",
        "no_description": "لا يوجد وصف.",
        "available_formats": "التنسيقات المتاحة",
        "best_video_format": "أفضل تنسيق فيديو فقط:",
        "best_audio_format": "أفضل تنسيق صوت فقط:",

        # ──────────────────────────────────────────────────────
        # نافذة معلومات الفيديو
        # ──────────────────────────────────────────────────────
        "video_info_title": "معلومات الفيديو",
        "text_summary": "ملخص نصي",
        "tab": "جدول",
        "detailed_summary": "ملخص تفصيلي",

        # ──────────────────────────────────────────────────────
        # الحالات ورسائل الحالة
        # ──────────────────────────────────────────────────────
        "ready_status": "جاهز",
        "loading_video_info": "جارٍ جلب معلومات الفيديو",
        "loading": "⏳ جارٍ التحميل...",
        "checking_url": "جارٍ التحقق من الرابط...",
        "download_started": "بدأ التنزيل",
        "downloading": "جارٍ التنزيل:",
        "remaining_time": "الوقت المتبقي:",
        "processing_file": "جارٍ معالجة الملف...",
        "canceling_download": "جارٍ إلغاء التنزيل...",
        "canceling_batch_download": "جارٍ إلغاء التنزيل الجماعي...",
        "no_file_in_the_queue": "لا توجد ملفات في قائمة الانتظار",

        # ──────────────────────────────────────────────────────
        # قوائم التشغيل
        # ──────────────────────────────────────────────────────
        "playlist_detected_singular": "📋 تم اكتشاف قائمة تشغيل: تم العثور على فيديو واحد. جارٍ التحميل...",
        "playlist_detected_plural": "📋 تم اكتشاف قائمة تشغيل: تم العثور على {count} فيديوهات. جارٍ التحميل...",
        "queue_added_singular": "✅ تمت إضافة فيديو واحد إلى قائمة الانتظار",
        "queue_added_plural": "✅ تمت إضافة {count} فيديوهات إلى قائمة الانتظار",

        # ──────────────────────────────────────────────────────
        # رسائل النجاح
        # ──────────────────────────────────────────────────────
        "download_complete": "اكتمل التنزيل",
        "download_complete_message": "تم إكمال التنزيل بنجاح!",
        "batch_download_complete": "اكتمل التنزيل الجماعي",
        "downloads_success_ratio_singular": "✅ تم تنزيل {success}/{total} ملف بنجاح",
        "downloads_success_ratio_plural": "✅ تم تنزيل {success}/{total} ملفات بنجاح",

        # ──────────────────────────────────────────────────────
        # رسائل الخطأ والتحذيرات
        # ──────────────────────────────────────────────────────
        "warning": "تحذير",
        "error": "خطأ",
        "error_prefix": "خطأ: ",
        "download_failed": "فشل التنزيل",
        "download_canceled": "تم إلغاء التنزيل",
        "partial_download_message": "لم يتم تنزيل بعض الملفات",
        "enter_valid_url": "يرجى إدخال رابط صالح",
        "no_valid_urls": "لم يتم العثور على روابط صالحة",
        "no_video": "لم يتم العثور على فيديو لهذا الرابط",
        "no_resolutions_found": "لم يتم العثور على دقات",
        "no_bitrates_found": "لم يتم العثور على معدلات بت",
        "fetching_impossible": "تعذر جلب معلومات الفيديو",
        "playlist_private": "قائمة تشغيل خاصة — يتطلب تسجيل الدخول. يرجى توفير ملفات تعريف الارتباط لـ YouTube.",

        # ──────────────────────────────────────────────────────
        # الملفات
        # ──────────────────────────────────────────────────────
        "select_output_folder": "اختر مجلد الإخراج",
        "select_cookies_file": "اختر ملف cookies.txt",
        "load_urls_list": "تحميل قائمة الروابط",
        "text_files": "ملفات نصية",
        "loaded_urls": "تم تحميل {count} رابط من الملف",
        "file_load_error": "خطأ في تحميل الملف: {error}",
        "cannot_read_file": "تعذر قراءة الملف: {error}",
        "download_folder": "التنزيلات",
    },

}