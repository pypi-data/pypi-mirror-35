import os
import json
import subprocess as sp


VIDEO_CODECS_SUPPORTED_BY_EXTENSION = {
    ".mkv": [
        "h264",        # V_MPEG4/ISO/AVC   | AV_CODEC_ID_H264
        "mpeg1video",  # V_MPEG1           | AV_CODEC_ID_MPEG1VIDEO
        "mpeg2video",  # V_MPEG2           | AV_CODEC_ID_MPEG2VIDEO
        "mpeg4",       # V_MPEG4/ISO/ASP   | AV_CODEC_ID_MPEG4
                       # V_MPEG4/ISO/AP    | AV_CODEC_ID_MPEG4
                       # V_MPEG4/ISO/SP    | AV_CODEC_ID_MPEG4
        "hevc",        # V_MPEGH/ISO/HEVC  | AV_CODEC_ID_HEVC 
        "msmpeg4v3",   # V_MPEG4/MS/V3     | AV_CODEC_ID_MSMPEG4V3 ???
        "prores",      # V_PRORES          | AV_CODEC_ID_PRORES ???
        "rv10",        # V_REAL/RV10       | AV_CODEC_ID_RV10 ???
        "rv20",        # V_REAL/RV20       | AV_CODEC_ID_RV20 ???
        "rv30",        # V_REAL/RV30       | AV_CODEC_ID_RV30 ???
        "rv40",        # V_REAL/RV40       | AV_CODEC_ID_RV40 ???
        "theora",      # V_THEORA          | AV_CODEC_ID_THEORA ???
        "rawvideo",    # V_UNCOMPRESSED    | AV_CODEC_ID_RAWVIDEO ???
        "vp8",         # V_VP8             | AV_CODEC_ID_VP8 ???
        "vp9",         # V_VP9             | AV_CODEC_ID_VP9 ???

        # "av1",         # V_AV1             | AV_CODEC_ID_AV1 ???
        # "dirac",       # V_DIRAC           | AV_CODEC_ID_DIRAC ???
        # "ffv1",        # V_FFV1            | AV_CODEC_ID_FFV1 ???
        # "mjpeg",       # V_MJPEG           | AV_CODEC_ID_MJPEG ??? (keep here?)
        # "snow",        # V_SNOW            | AV_CODEC_ID_SNOW ???
    ],
    ".m4v": [
        "h264",        # V_MPEG4/ISO/AVC   | AV_CODEC_ID_H264
        "mpeg4",       # V_MPEG4/ISO/ASP   | AV_CODEC_ID_MPEG4
        "hevc",        # V_MPEGH/ISO/HEVC  | AV_CODEC_ID_HEVC 
        # "mpeg1video",  # V_MPEG1           | AV_CODEC_ID_MPEG1VIDEO
        # "mpeg2video",  # V_MPEG2           | AV_CODEC_ID_MPEG2VIDEO

        # "mjpeg",       # V_MJPEG           | AV_CODEC_ID_MJPEG ??? (keep here?)
        # "png",         #                   | AV_CODEC_ID_PNG ??? (keep here?)
        # "jpeg2000",    #                   | AV_CODEC_ID_JPEG2000 ??? (keep here?)
        # "vc1image",    #                   | AV_CODEC_ID_VC1 ??? (keep here?)
        # "dirac",       # V_DIRAC           | AV_CODEC_ID_DIRAC ???
        # "tscc2",       #                   | AV_CODEC_ID_TSCC2 ???
        # "vp8",         # V_VP8             | AV_CODEC_ID_VP8 ???
        # "vp9",         # V_VP9             | AV_CODEC_ID_VP9 ???
        # "theora",      # V_THEORA          | AV_CODEC_ID_THEORA ???

    ],
    ".mp4": [
        "h264",        # V_MPEG4/ISO/AVC   | AV_CODEC_ID_H264
        "mpeg4",       # V_MPEG4/ISO/ASP   | AV_CODEC_ID_MPEG4
        "hevc",        # V_MPEGH/ISO/HEVC  | AV_CODEC_ID_HEVC 
    ],
    ".avi": [
        "mpeg4",    # AV_CODEC_ID_MPEG4
        "mpeg1video",  # V_MPEG1           | AV_CODEC_ID_MPEG1VIDEO
        "mpeg2video",  # V_MPEG2           | AV_CODEC_ID_MPEG2VIDEO
        "mpeg4",    # AV_CODEC_ID_MPEG4
        "h264",     # AV_CODEC_ID_H264 ???
        # "rawvideo", # AV_CODEC_ID_RAWVIDEO ???
        # "vp8",         # V_VP8             | AV_CODEC_ID_VP8 ???
    ],
}

AUDIO_CODECS_SUPPORTED_BY_EXTENSION = {
    ".mkv": [
        "ac3",              # A_AC3             | AV_CODEC_ID_AC3
        "aac",              # A_AAC             | AV_CODEC_ID_AAC
        "alac",             # A_ALAC            | AV_CODEC_ID_ALAC
        "dts",              # A_DTS             | AV_CODEC_ID_DTS
        "eac3",             # A_EAC3            | AV_CODEC_ID_EAC3 ???
        "flac",             # A_FLAC            | AV_CODEC_ID_FLAC
        "mlp",              # A_MLP             | AV_CODEC_ID_MLP" ???
        "mp2",              # A_MPEG/L2         | AV_CODEC_ID_MP2
        "mp1",              # A_MPEG/L1         | AV_CODEC_ID_MP1
        "mp3",              # A_MPEG/L3         | AV_CODEC_ID_MP3
        "opus",             # A_OPUS            | AV_CODEC_ID_OPUS ???
        "pcm_f32le",        # A_PCM/FLOAT/IEEE  | AV_CODEC_ID_PCM_F32LE ???
        "pcm_f64le",        # A_PCM/FLOAT/IEEE  | AV_CODEC_ID_PCM_F64LE ???
        "pcm_s16be_planar", # A_PCM/INT/BIG     | AV_CODEC_ID_PCM_S16BE ???
        "pcm_s24be",        # A_PCM/INT/BIG     | AV_CODEC_ID_PCM_S24BE ???
        "pcm_s32be",        # A_PCM/INT/BIG     | AV_CODEC_ID_PCM_S32BE ???
        "pcm_s16le",        # A_PCM/INT/LIT     | AV_CODEC_ID_PCM_S16LE ???
        "pcm_s24le",        # A_PCM/INT/LIT     | AV_CODEC_ID_PCM_S24LE ???
        "pcm_s32le",        # A_PCM/INT/LIT     | AV_CODEC_ID_PCM_S32LE ???
        "pcm_u8",           # A_PCM/INT/LIT     | AV_CODEC_ID_PCM_U8 ???
        "qdmc",             # A_QUICKTIME/QDMC  | AV_CODEC_ID_QDMC ???
        "qdm2",             # A_QUICKTIME/QDM2  | AV_CODEC_ID_QDM2 ???
        "ra_144",           # A_REAL/14_4       | AV_CODEC_ID_RA_144 ???
        "ra_288",           # A_REAL/28_8       | AV_CODEC_ID_RA_288 ???
        "atrac3p",          # A_REAL/ATRC       | AV_CODEC_ID_ATRAC3 ???
        "cook",             # A_REAL/COOK       | AV_CODEC_ID_COOK ???
        "sipr",             # A_REAL/SIPR       | AV_CODEC_ID_SIPR ???
        "truehd",           # A_TRUEHD          | AV_CODEC_ID_TRUEHD ???
        "tta",              # A_TTA1            | AV_CODEC_ID_TTA ???
        "vorbis",           # A_VORBIS          | AV_CODEC_ID_VORBIS
        "wavpack",          # A_WAVPACK4        | AV_CODEC_ID_WAVPACK
        ],
    ".m4v": [
        "aac",              # A_AAC             | AV_CODEC_ID_AAC
        "alac",             # A_ALAC            | AV_CODEC_ID_ALAC
        # "mp2",              # A_MPEG/L2         | AV_CODEC_ID_MP2
        # "vorbis",           # A_VORBIS          | AV_CODEC_ID_VORBIS
        # "mp3",              # A_MPEG/L3         | AV_CODEC_ID_MP3
        # "mp4als",           #                   |  AV_CODEC_ID_MP4ALS
        # "ac3",              # A_AC3             | AV_CODEC_ID_AC3
        # "eac3",             # A_EAC3            | AV_CODEC_ID_EAC3 ???
        # "opus",             # A_OPUS            | AV_CODEC_ID_OPUS ??
    ],
    ".mp4": [
        "aac",              # A_AAC             | AV_CODEC_ID_AAC
        "alac",             # A_ALAC            | AV_CODEC_ID_ALAC
    ],
    ".avi": [
        "mp3", # AV_CODEC_ID_MP3
        "mp2", # AV_CODEC_ID_MP2
        # "ac3", # AV_CODEC_ID_AC3 ???
        # "dts",              # A_DTS             | AV_CODEC_ID_DTS ???
    ],
    
    ".ac3": [
        "ac3",              # A_AC3             | AV_CODEC_ID_AC3
    ],
    ".aac": [
        "aac",              # A_AAC             | AV_CODEC_ID_AAC
    ],
}

SUBTITLE_CODECS_SUPPORTED_BY_EXTENSION = {
    ".mkv": [
        "subrip",                # S_TEXT/UTF8            | AV_CODEC_ID_SUBRIP
        "webvtt",                # D_WEBVTT/SUBTITLES     | AV_CODEC_ID_WEBVTT ???
                                 # D_WEBVTT/CAPTIONS      | AV_CODEC_ID_WEBVTT
                                 # D_WEBVTT/DESCRIPTIONS  | AV_CODEC_ID_WEBVTT
                                 # D_WEBVTT/METADATA      | AV_CODEC_ID_WEBVTT
        "text",                  # S_TEXT/UTF8            | AV_CODEC_ID_TEXT ???
                                 # S_TEXT/ASCII           | AV_CODEC_ID_TEXT
        "ass",                   # S_TEXT/ASS             | AV_CODEC_ID_ASS ???
                                 # S_TEXT/SSA             | AV_CODEC_ID_ASS
                                 # S_ASS                  | AV_CODEC_ID_ASS
                                 # S_SSA                  | AV_CODEC_ID_ASS
        "dvd_subtitle",          # S_VOBSUB               | AV_CODEC_ID_DVD_SUBTITLE ???
        "dvb_subtitle",          # S_DVBSUB               | AV_CODEC_ID_DVB_SUBTITLE ???
        "hdmv_pgs_subtitle",     # S_HDMV/PGS             | AV_CODEC_ID_HDMV_PGS_SUBTITLE ???
        "hdmv_text_subtitle",    # S_HDMV/TEXTST          | AV_CODEC_ID_HDMV_TEXT_SUBTITLE ???
    ],
    ".m4v": [
        "mov_text", # AV_CODEC_ID_MOV_TEXT
        # "dvd_subtitle",          # S_VOBSUB               | AV_CODEC_ID_DVD_SUBTITLE ???
    ],
    ".mp4": [
        "mov_text", # AV_CODEC_ID_MOV_TEXT
    ],
    
    ".srt": [
        "subrip",                # S_TEXT/UTF8            | AV_CODEC_ID_SUBRIP
    ],
}



# valid output extensions
SUPPORTED_VIDEO_EXTENSIONS = [".mkv", ".m4v", ".mp4"]
SUPPORTED_AUDIO_EXTENSIONS = [".aac", ".ac3"]
SUPPORTED_SUBTITLE_EXTENSIONS = [".srt"]

SUPPORTED_EXTENSIONS = \
    SUPPORTED_VIDEO_EXTENSIONS + \
    SUPPORTED_AUDIO_EXTENSIONS + \
    SUPPORTED_SUBTITLE_EXTENSIONS

SUPPORTED_VIDEO_CODECS = ['h264', 'h265']
SUPPORTED_AUDIO_CODECS = ["aac", "ac3", "flac"]
SUPPORTED_SUBTITLE_CODECS = ["mov_text", "subrip", "srt",]

IMAGES_CODECS = [
    'mjpeg', 'jpeg2000', 'jpegls', 'mjpegb', 'ljpeg', 
    'gif', 'tiff', "png",
]


def check_ffmpeg():
    try:
        import os
        sp.run([os.environ.get("FFMPEG_BINARY", "ffmpeg"), '-loglevel', 'quiet'])
    except FileNotFoundError:
        raise FileNotFoundError("Shane requires FFmpeg installed.")


def choose_codec(stream, dst_extension):
    assert dst_extension in SUPPORTED_EXTENSIONS
    
    if stream.is_inner:
        src_extension = stream.container.default_extension
    else:
        src_extension = stream.default_extension

    if stream.codec != stream.default_codec:
        return stream.codec
    else:
        if dst_extension == src_extension:
            return "copy"

    if _is_supported_by_extension(dst_extension, stream):
        return "copy"

    else:
        return _get_default_codec(dst_extension, stream)



def _is_supported_by_extension(extension, stream):
    assert stream.is_video or stream.is_audio or stream.is_subtitle, f"Stream: {stream.codec}"
    if stream.is_video:
        supported_codecs = VIDEO_CODECS_SUPPORTED_BY_EXTENSION[extension]
    elif stream.is_audio:
        supported_codecs = AUDIO_CODECS_SUPPORTED_BY_EXTENSION[extension]
    elif stream.is_subtitle:
        supported_codecs = SUBTITLE_CODECS_SUPPORTED_BY_EXTENSION[extension]
    return stream.codec in supported_codecs



def _get_default_codec(extension, stream):
    assert stream.is_video or stream.is_audio or stream.is_subtitle, f"Stream: {stream.codec}"
    try:
        if stream.is_video:
            default_codec = VIDEO_CODECS_SUPPORTED_BY_EXTENSION[extension][0]
        elif stream.is_audio:
            default_codec = AUDIO_CODECS_SUPPORTED_BY_EXTENSION[extension][0]
        elif stream.is_subtitle:
            default_codec = SUBTITLE_CODECS_SUPPORTED_BY_EXTENSION[extension][0]
    except KeyError:
        raise ExtentionError(f"The extension {extension} doesn't support")
    return default_codec


    
class ExtentionError(Exception):
    pass