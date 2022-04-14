def mediatype(media):
    if media.endswith(".jpg"):
        return 'image/jpg'
    elif media.endswith(".png"):
        return 'image/png'
    elif media.endswith(".css"):
        return 'text/css'
    elif media.endswith(".aac"):
        return 'audio/aac'
    elif media.endswith(".abw"):
        return 'application/x-abiword'
    elif media.endswith(".arc"):
        return 'document(multiple files embedded)	application/x-freearc'
    elif media.endswith(".avif"):
        return 'image/avif'
    elif media.endswith(".avi"):
        return 'video/x-msvideo'
    elif media.endswith(".azw"):
        return 'application/vnd.amazon.ebook'
    elif media.endswith(".bin"):
        return 'application/octet-stream'
    elif media.endswith(".bmp"):
        return 'image/bmp'
    elif media.endswith(".bz"):
        return 'application/x-bzip'
    elif media.endswith(".bz2"):
        return 'application/x-bzip2'
    elif media.endswith(".cda"):
        return 'application/x-cdf'
    elif media.endswith(".csh"):
        return 'application/x-csh'
    elif media.endswith(".csv"):
        return 'text/csv'
    elif media.endswith(".doc"):
        return 'application/msword'
    elif media.endswith(".docx"):
        return 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    elif media.endswith(".eot"):
        return 'application/vnd.ms-fontobject'
    elif media.endswith(".epub"):
        return 'application/epub+zip'
    elif media.endswith(".gz"):
        return 'application/gzip'
    elif media.endswith(".gif"):
        return 'image/gif'
    elif media.endswith(".ico"):
        return 'image/vnd.microsoft.icon'
    elif media.endswith(".ics"):
        return 'text/calendar'
    elif media.endswith(".jar"):
        return 'application/java-archive'
    elif media.endswith(".jpeg"):
        return 'image/jpeg'
    elif media.endswith(".js"):
        return 'text/javascript'
    elif media.endswith(".json"):
        return 'application/json'
    elif media.endswith(".jsonld"):
        return 'application/ld+json'
    elif media.endswith(".mp3"):
        return 'audio/mpeg'
    elif media.endswith(".mp4"):
        return 'video/mp4'
    elif media.endswith(".mpeg"):
        return 'video/mpeg'
    elif media.endswith(".png"):
        return 'image/png'
    elif media.endswith(".pdf"):
        return 'application/pdf'
    elif media.endswith(".php"):
        return 'application/x-httpd-php'
    elif media.endswith(".ppt"):
        return 'application/vnd.ms-powerpoint'
    elif media.endswith(".pptx"):
        return 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    elif media.endswith(".rar"):
        return 'application/vnd.rar'
    elif media.endswith(".rtf"):
        return 'application/rtf'
    elif media.endswith(".svg"):
        return 'image/svg+xml'
    elif media.endswith(".tar"):
        return 'application/x-tar'
    elif media.endswith(".tif"):
        return 'image/tiff'
    elif media.endswith(".ts"):
        return 'video/mp2t'
    elif media.endswith(".wav"):
        return 'audio/wav'
    elif media.endswith(".xls"):
        return 'application/vnd.ms-excel'
    elif media.endswith(".xlsx"):
        return 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    elif media.endswith(".xml"):
        return 'application/xml'
    elif media.endswith(".zip"):
        return 'application/zip'
    else:
        return 'text/html'
