import os
import json
import subprocess as sp

import shane
from shane._rules import INPUT_RULES, OUTPUT_RULES



class FFprobe:
    BINARY = os.environ.get("FFPROBE_BINARY", "ffprobe")
    LOGLEVEL = "quiet"
    PRINT_FORMAT = "json"

    _BINARY = [BINARY]
    _LOGLEVEL = ["-loglevel", LOGLEVEL]
    _PRINT_FORMAT = ["-print_format", PRINT_FORMAT]

    def __init__(self, path):
        self._path_cmd = ["-i", str(path)]

    @property
    def _base_cmd(self) -> list:
        return self._BINARY + self._LOGLEVEL + self._PRINT_FORMAT

    def run(self, args=[]) -> dict:
        assert isinstance(args, list)
        command = self._base_cmd + args + self._path_cmd
        response = sp.check_output(command)
        return json.loads(response)

    def get_all(self) -> dict:
        args = ["-show_streams", "-show_chapters", "-show_format"]
        return self.run(args)

    def get_format(self) -> dict:
        return self.get_all()["format"]

    def get_streams(self) -> list:
        return self.get_all()["streams"]
    
    def get_first_stream(self) -> list:
        return self.get_streams()[0]

    def get_chapters(self) -> list:
        return self.get_all()["chapters"]



class FFmpeg:
    BINARY = os.environ.get("FFMPEG_BINARY", "ffmpeg")
    LOGLEVEL = "quiet"
    PRINT_FORMAT = "json"
    OVERWRITE = "-y"


    _BINARY = [BINARY]
    _LOGLEVEL = ["-loglevel", LOGLEVEL]
    _OVERWRITE = [OVERWRITE]
    
    def __init__(self, inputs, outputs):
        self._inputs = inputs
        self._outputs = outputs
    
    @property
    def commandlist(self) -> list:
        command = []
        command += self._BINARY + self._LOGLEVEL + self._OVERWRITE
        command += self._merge(self._inputs, is_input=True)
        command += self._merge(self._outputs)
        return command

    @property
    def commandstring(self) -> str:
        return sp.list2cmdline(self.commandlist)

    def run(self):
        return sp.run(self.commandlist)

    def _merge(self, dict_commands: dict, is_input=False) -> list:
        commands = []
        for argument, options in dict_commands.items():
            commands.extend(options)
            if is_input:
                commands.append("-i")
            commands.append(argument)
        return commands


class FFmpegMiddleware:
    """`Container`/`Stream` -> `FFmpegMiddleware` -> `FFmpeg`"""

    def __init__(self, src, dst, settings={}):
        # src — Stream or Container as an input
        # dst - Stream ot Container as an output
        self.src = src
        self.dst = dst
        self.settings = settings
    
    @property
    def input_files(self) -> list:
        if isinstance(self.src, shane._container.Container):
            if self.src.default_path is not None:
                # self container + outer streams
                return [self.src] + [s for s in self.src.streams if not s.is_inner]
            else:
                # only outer streams
                return [s for s in self.src.streams if not s.is_inner]
        else:
            return [self.src]

    def inputs(self) -> dict:
        """Returns a `dict` with ffmpeg input commands"""
        inputs = {}
        for input_file in self.input_files:
            path = input_file.default_path
            commands = self._generate_input_commands(input_file)
            inputs[path] = commands
        return inputs

    def outputs(self) -> dict:
        """Returns a `dict` with ffmpeg output commands"""
        outputs = {}
        for input_file in self.input_files:
            if isinstance(input_file, shane._streams.Stream):
                files = [input_file]
            else:
                files = [input_file] + [s for s in input_file.streams if s.is_inner]
            path = input_file.path
            outputs[path] = []
            for f in files:
                outputs[path] += self._generate_output_commands(f)
        return outputs

    def _generate_input_commands(self, input_file):
        commands = []
        for rule in INPUT_RULES:
            commands += rule(input_file=input_file)
        return commands

    def _generate_output_commands(self, input_file):
        commands = []
        for rule in OUTPUT_RULES:
            i_s = self._get_input_specifier_index_for(input_file)
            o_s = self._get_output_specifier_index_for(input_file)
            commands += rule(
                input_file=input_file,
                output_file=self.dst,
                input_specifier=i_s,
                output_specifier=o_s,  # don't exist if container
                settings=self.settings,
            )
        return commands

    def _get_output_specifier_index_for(self, x):
        o = 0
        for input_file in self.input_files:
            if isinstance(input_file, shane._container.Container):
                for stream in input_file.streams:
                    if x == stream:
                        return o
                    o += 1
            else:
                if x == input_file:
                    return o
                o += 1

    def _get_input_specifier_index_for(self, x):
        only_default_streams = lambda x: x.container is input_file
        for i, input_file in enumerate(self.input_files):
            if isinstance(input_file, shane._container.Container):
                for stream in filter(only_default_streams, input_file.streams):
                    if x == stream:
                        return i
            else:
                if x == input_file:
                    return i


# def vstream_with_changed_fps(stream):
#     return stream.default_fps != stream.fps


# def vstream_with_changed_frame_size(stream):
#     return stream.default_height != stream.height or \
#     stream.default_width != stream.width



# def codec_if_convert_to_extension(stream, output_extension):
#     if stream.is_video:
#         possible_codecs_for = VIDEO_CODECS_SUPPORTED_BY_EXTENSION
#         supported_extensions = SUPPORTED_VIDEO_EXTENSIONS
    
#     elif stream.is_audio:
#         possible_codecs_for = AUDIO_CODECS_SUPPORTED_BY_EXTENSION
#         supported_extensions = (
#             SUPPORTED_VIDEO_EXTENSIONS + SUPPORTED_AUDIO_EXTENSIONS
#         )
    
#     elif stream.is_subtitle:
#         possible_codecs_for = SUBTITLE_CODECS_SUPPORTED_BY_EXTENSION
#         supported_extensions = (
#             SUPPORTED_VIDEO_EXTENSIONS + SUPPORTED_SUBTITLE_EXTENSIONS
#         )
    
#     # elif stream.is_image:
#     #     raise NotImplementedError
    
#     # elif stream.is_attachment:
#     #     raise NotImplementedError
    
#     # elif stream.is_data:
#     #     raise NotImplementedError
    
#     # else:
#     #     raise NotImplementedError
    
#     for supported_extension in supported_extensions:
#         if supported_extension == output_extension:
#             if stream.codec in possible_codecs_for[output_extension]:
#                 return 'copy'
#             else:
#                 return possible_codecs_for[output_extension][0] # default codec
    
#     raise ValueError(
#         f"Can't return codec for the extension '{output_extension}'"
#     )



# class FFmpegCompressorError(Exception):
#     pass


# class FFmpegCompressor:
#     BINARY = os.environ.get("FFMPEG_BINARY", "ffmpeg")
#     LOGLEVEL = "quiet"
#     PRINT_FORMAT = "json"

#     _BINARY = [BINARY]
#     _LOGLEVEL = ["-loglevel", LOGLEVEL]
#     _PRINT_FORMAT = ["-print_format", PRINT_FORMAT]
    
#     def __init__(self):
#         self.input_files = None
#         self.settings = {}
#         # one inner list for one input file
#         self.input_paths = []
#         self.input_commands = [] 
        
#         self.output_path = None
#         self.output_commands = []
        
#         self.stream_commands_functions = [
#             # common
#             self.command_codec,
#             self.command_map,
#             self.command_metadata,
#             # only video
#             self.command_fps,
#             self.command_frame_size,
#             self.command_vtag,
#         ]
#         self.container_commands_functions = [
#             self.command_metadata,
#         ]
#         self.global_commands_functions = [
#             self.command_crf,
#         ]

#     @property
#     def output_path_extension(self):
#         return os.path.splitext(self.output_path)[-1]
    
#     @property
#     def command_without_output_path(self):
#         cmd = []
#         cmd += self._BINARY
#         for i in range(len(self.input_paths)):
#             cmd += self.input_commands[i]
#             cmd += self.input_paths[i]
#         cmd += self.output_commands
#         # cmd += [self.output_path]
#         return cmd

#     def add_input_files(self, *input_files):
#         self.input_files = list(input_files)

#     def _generate_common_command(self):
#         if self.input_files is None:
#             raise FFmpegCompressorError(
#                 'FFmpegCompressor requires input files.'
#             )
#         for input_file in self.input_files:
#             self.input_paths.append(
#                 ['-i', input_file.default_path]
#             )
#             self.input_commands.append(
#                 list(self._generate_input_commands(input_file))
#             )
#             self.output_commands.extend(
#                 list(self._generate_output_commands(input_file))
#             )
#         return self.command_without_output_path
    
#     def _generate_command_for_extracting_stream(self, stream):
#         if self.input_files is None:
#             raise FFmpegCompressorError(
#                 'FFmpegCompressor requires input files.'
#             )
#         if len(self.input_files) > 1:
#             raise FFmpegCompressorError(
#                 f'To select a stream you need one input file, but received \
#                 {len(self.input_files)}'
#             )
#         container = self.input_files[0]

#         self.input_paths.append(['-i', container.default_path])
#         self.input_commands.append(
#                 list(self._generate_input_commands(container))
#             )
#         self.output_commands.extend(
#                 list(self._generate_output_commands(stream))
#             )
#         return self.command_without_output_path

#     def add_output_path(self, path):
#         self.output_path = path
    
#     def add_settings(self, **settings):
#         self.settings = settings

#     def _run_command(self, command, temp_output_path):
#         command.append(temp_output_path)
#         # print(sp.list2cmdline(command))
#         response = sp.run(command)
#         if response:
#             self._remove_and_rename_path(temp_output_path, self.output_path)
#         return response

#     def run(self):
#         self._run_command(
#             self._generate_common_command(),
#             self._choose_temp_path(self.output_path)
#             )

#     def extract_stream_run(self, stream):
#         self._run_command(
#             self._generate_command_for_extracting_stream(stream),
#             self._choose_temp_path(self.output_path)
#             )
    
#     def _remove_and_rename_path(self, temp_path, path):
#         if temp_path != path:
#             os.remove(path)
#             os.rename(temp_path, path)    
    
#     def _choose_temp_path(self, default_path):
#         if not os.path.exists(default_path):
#             return default_path
#         i = 1
#         root, ext = os.path.splitext(default_path)
#         temp_path = f"{root} (temp {i}){ext}"
#         while os.path.exists(temp_path):
#             i += 1
#             temp_path = f"{root} (temp {i}){ext}"
#         return temp_path
    
#     def _generate_input_commands(self, input_file):
#         commands = []
#         if input_file.is_container and input_file.default_extension == '.avi':
#             commands += ['-fflags', '+genpts']
#         return commands

#     def _generate_output_commands(self, input_file):
#         if input_file.is_container:
#             streams = [s for s in input_file.streams if s.is_inner]
#             container = input_file
#         else:
#             streams = [input_file]
#             container = None
#         # stream commands
#         for command_function in self.stream_commands_functions:
#             for stream in streams:
#                 yield from command_function(stream)
#         # container commands
#         if container:
#             for command_function in self.container_commands_functions:
#                 yield from command_function(container)
#         # global container commands
#             for command_function in self.global_commands_functions:
#                 yield from command_function()

#     # COMMANDS

#     def command_codec(self, x):
#         if x.is_attachment or x.is_image or x.is_data:
#             return []
#         extension = self._get_output_extension()
#         option = f"-{x.type[0]}codec:{x.index}" 
#         argument = codec_if_convert_to_extension(x, extension)
#         if x.is_video and \
#         (vstream_with_changed_fps(x) or vstream_with_changed_frame_size(x)):
#             argument = x.codec
#         return [option, argument]

#     def command_map(self, x):
#         if (x.is_attachment or x.is_image or x.is_data) and not self._keep(x):
#             return []
#         i_s_i = self._get_input_specifier_index_for(x)
#         return ["-map", f"{i_s_i}:{x.index}"]
    
#     def command_metadata(self, x):
#         if not x.is_container:
#             if (x.is_attachment or x.is_image or x.is_data) and not self._keep(x):
#                 return []
#             o_s_i = f':s:{self._get_output_specifier_index_for(x)}'
#         else:
#             o_s_i = ''
#         result = []
#         for key, value in x.metadata.items():
#             result += [f"-metadata{o_s_i}", f"{key}={value}"]
#         return result
    
#     def command_fps(self, x):
#         if not x.is_video:
#             return []
#         i_s_i = self._get_input_specifier_index_for(x)
#         if vstream_with_changed_fps(x):
#             return [f"-r:{i_s_i}:{x.index}", x.fps]
#         else:
#             return []
    
#     def command_frame_size(self, x):
#         if not x.is_video:
#             return []
#         i_s_i = self._get_input_specifier_index_for(x)
#         if vstream_with_changed_frame_size(x):
#             return [f'-s:{i_s_i}:{x.index}', f"{x.width}x{x.height}"]
#         else:
#             return []
    
#     def command_crf(self):
#         if self.settings.get('crf'):
#             return ['-crf', self.settings['crf']]
#         else:
#             return []
    
#     def command_vtag(self, x):
#         if not x.is_video:
#             return []
#         extension = self._get_output_extension()
#         codec = codec_if_convert_to_extension(x, extension)
#         if codec == 'copy':
#             codec = x.codec
#         is_m4v_or_mp4 = (extension == '.m4v' or extension == '.mp4')
#         is_hevc = codec in ['libx265', 'hevc']
#         if is_hevc and is_m4v_or_mp4:
#             return ['-vtag', 'hvc1'] 
#         else:
#             return []
     
#     def _get_output_specifier_index_for(self, x):
#         o = 0
#         for input_file in self.input_files:
#             if input_file.is_container:
#                 for stream in input_file.streams:
#                     if x == stream:
#                         return o
#                     o += 1
#             else:
#                 if x == input_file:
#                     return o
#                 o += 1

#     def _get_input_specifier_index_for(self, x):
#         for i, input_file in enumerate(self.input_files):
#             if input_file.is_container:
#                 for stream in filter(lambda x: x.container is input_file, input_file.streams):
#                     if x == stream:
#                         return i
#             else:
#                 if x == input_file:
#                     return i
    
#     def _get_output_extension(self):
#         return os.path.splitext(self.output_path)[-1]

#     def _keep(self, x):
#         for c in (c for c in self.input_files if c.is_container):
#             if c.streams.index(x):
#                 if c.default_extension == self.output_path_extension:
#                     return True
