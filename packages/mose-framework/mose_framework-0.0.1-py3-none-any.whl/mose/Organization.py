from __future__ import annotations
from modified_json_tricks import loads, dumps
from typing import Union, Tuple, List, Optional
import os
from collections import OrderedDict
from datetime import date, datetime
import pickle as pkl
import numpy as np
import pandas as pd
from IPython import get_ipython
import pathlib
from tqdm import tqdm
from Imaging.IO import save_raw_binary, determine_bruker_folder_contents
from Management.UserInterfaces import select_directory, verbose_copying


class Study:
    def __init__(self):
        pass


class Mouse:
    """
    Class for organizing & managing experimental data within one mouse.

    **Keyword Arguments**
        | *Logfile* : Path to existing log file (str, default None)
        | *Mouse* : Mouse ID (str, default None)
        | *Condition* : Experimental Condition (str, default None)
        | *Directory* : Directory for hierarchy (str, default None)
        | *Study* : Study (str, default None)
        | *StudyMouse* : Study ID (str, default None)

    **Properties**
        | *experimental_condition* : Experiment condition of the mouse
        | *log_file* : Log Filename Path
        | *instance_data* : Date when this experimental hierarchy was created
        | *mouse_id* : ID of Mouse

    **Attributes**
        | *directory* : Experimental Hierarchy Directory
        | *experiments* : Names of included experiments
        | *modifications* : modifications made to this file
        | *study* : Study
        | *study_mouse* : ID of mouse in study

    **Public Class Methods**
        | *load* : Function that loads the entire mouse

    **Public Methods**
        | *create* : This function creates the directory/logs/organization.json if it doesn't exist
        | *check_log* : Checks Log Status
        | *create_log_file* : Creates log file
        | *pass_meta* : Passes directory/mouse id
        | *record_mod* : Record modification of experiment
        | *record_experiments_mod* : Record modification of experiments
        | *save* : Saves mouse to organization.json
        | *start_log* : Starts Log

    **Private Class Methods**
        | *_generate_analysis_subdirectory* : Generate Analysis
        | *_generate_analysis_technique_subdirectory* : Generate Analysis Technique
        | *_generate_behavior_subdirectory* : Generate Behavioral Folder
        | *_generate_directory_structure* : Generates the Directory Structure (The structured folders where data stored)
        | *_generate_experiment_folders* : Generate Behavioral ExperimentName Folder
        | *_generate_histology_directory* :  Generates Histology Folder
        | *_generate_imaging_subdirectory* : Generate Imaging Folder
        | *_generate_roi_matching_index_directory* : Generate ROI Matching Folder

    """

    def __init__(self, **kwargs):
        """
        :keyword LogFile: Path to existing log file (str, default None)
        :keyword Mouse: Mouse ID (str, default None)
        :keyword Condition: Experimental Condition (str, default None)
        :keyword Directory: Directory for hierarchy (str, default None)
        :keyword Study: Study (str, default None)
        :keyword StudyMouse: Study ID (str, default None)
        """
        # Hidden
        self._mouse_id = None
        self._experimental_condition = None
        self._log_file = None

        # Protected In Practice
        self.log_file = kwargs.get('LogFile', None)
        self.mouse_id = kwargs.get('Mouse', None)
        self.experimental_condition = kwargs.get('Condition', None)
        self.__instance_date = get_date()
        #
        self.directory = kwargs.get('Directory', None)
        self.study = kwargs.get('Study', None)
        self.study_mouse = kwargs.get('StudyMouse', None)
        self.modifications = [(get_date(), get_time())]
        self.experiments = []

        # Create log file if one does not exist
        if self.log_file is None and self.mouse_id is not None:
            if self.directory is None:
                self.directory = os.getcwd()
            self.create()



        # start logging if log file exists
        if self.log_file is not None:
            self.start_log()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_log()

    @property
    def experimental_condition(self) -> str:
        """
        Experiment condition of the mouse

        :rtype: str
        """
        return self._experimental_condition

    @experimental_condition.setter
    def experimental_condition(self, Condition: str) -> Self:
        if self._experimental_condition is None and Condition is not None:
            self._experimental_condition = Condition
        else:
            print("Experimental condition can only be assigned ONCE.")

    @property
    def log_file(self) -> str:
        """
        Log Filename Path

        :rtype: str
        """
        return self._log_file

    @log_file.setter
    def log_file(self, LogFile: str) -> Self:
        if self._log_file is None and LogFile is not None:
            self._log_file = LogFile
        else:
            print("Log file can only be assigned ONCE.")

    @property
    def mouse_id(self) -> str:
        """
        ID of Mouse

        :rtype: str
        """
        return self._mouse_id

    @mouse_id.setter
    def mouse_id(self, ID: str) -> Self:
        # This is a way to adjust if you really wanted to
        if self._mouse_id is None and ID is not None:
            self._mouse_id = ID
        else:
            print("Mouse ID can only be set ONCE.")

    @property
    def instance_date(self) -> str:
        """
        Date when this experimental hierarchy was created

        :rtype: str
        """
        return self._Mouse__instance_date

    # noinspection All
    def check_log(self) -> Self:  # noinspection All
        """
        Checks log status

        :rtype: Any
        """

        self._IP.run_line_magic('logstate', '')

    def create(self) -> Self:
        """
        This function generates the directory hierarchy in one step

        :rtype: Any
        """

        if not os.path.exists(self.directory):
            try:
                os.makedirs(self.directory)
            except FileExistsError:
                pass
            self.create_log_file()
        if self.directory is not None:
            try:
                os.makedirs(self.directory + "\\LabNotebook")
            except FileExistsError:
                pass
            self.save()
        else:
            print("Unable to create organized directory in specified path.")

    def create_log_file(self) -> Self:
        """
        Creates log file

        :rtype: Any
        """
        if self.directory is not None:
            self.log_file = self.directory + "\\log_file.log"
            if not os.path.exists(self.directory):
                print("Could not locate directory, saving in base.")
                self.log_file = "".join([os.getcwd(), "\\log_file.log"])
        else:
            print("Could not locate directory, saving in base.")
            self.log_file = "".join([os.getcwd(), "\\log_file.log"])


        with open(self.log_file, "w") as _log:
            _log.write("")
        _log.close()

        print("Logging file assigned as :" + self.log_file)

    def create_experiment(self, ExperimentName: str, Type: Optional[str, Experiment] = "Experiment", **kwargs) -> Self:
        """
        Generates an experiment ExperimentName folder and attribute

        Kwargs are passed to underlying functions

        :param ExperimentName: Name of experimental ExperimentName
        :type ExperimentName: str
        :param Type: Type of experiment (Optional, default = Experiment)
        :type Type: Optional[str, Experiment]
        :rtype: Any
        """
        # Construct Folder
        # noinspection PyArgumentList
        self._generate_experiment_folders(ExperimentName, **kwargs)

        # Construct Class Instance as Attribute
        if isinstance(Type, str):
            _type_constructor = "".join([Type, "(self.pass_meta(), ExperimentName)"])
            setattr(self, ExperimentName, eval(_type_constructor))
        elif issubclass(Type, Experiment):
            # noinspection PyCallingNonCallable
            setattr(self, ExperimentName, Type(self.pass_meta(), ExperimentName))
        else:
            raise TypeError("Unable to determine specified Type of experiment. Make sure the Type is imported")

        # Record-Keeping
        self.experiments.append(ExperimentName)
        self.record_mod("".join(["Added ", ExperimentName]))
        self.record_experiment_mod(ExperimentName, "Instanced using create_experiment")

        # if interactive
        _interactive = kwargs.get("interactive", True)
        if _interactive:
            # noinspection PyProtectedMember
            self.__getattribute__(ExperimentName).copy_data()

    # noinspection All
    def end_log(self) -> Self:
        """
        Ends Logging

        :rtype: Any
        """
        self._IP.run_line_magic('logstop', '')

    def pass_meta(self) -> Tuple[str, str]:
        """
        Passes directory/mouse id

        :returns: directory/mouse id
        :rtype: tuple[str, str]
        """

        return self.directory, self.mouse_id

    def record_mod(self, *args: str) -> Self:
        """
        Record modification of experiment (Data, Time, *args)


        :param args: A string explaining the modification
        :type args: str
        :rtype: Any
        """

        # noinspection PyTypeChecker
        self.modifications.append((get_date(), get_time(), *args))

    def record_experiment_mod(self, ExperimentNameKey: str, *args) -> Self:
        """
        Record modification of experiment (Data, Time, *args)

        :param ExperimentNameKey: The key name for the ExperimentName
        :type ExperimentNameKey: str
        :param args: A string explaining the modification
        :type args: str
        :rtype: Any
        """

        if args:
            self.record_mod(args[0])
        else:
            self.record_mod()
        try:
            self.__dict__.get(ExperimentNameKey).record_mod()
        except KeyError:
            print("Unable to identify ExperimentName from provided key")

    def save(self) -> Self:
        """
        Saves Mouse to json

        :rtype: Any
        """

        print("Saving mouse...")
        if hasattr('self', '_IP'):
            # noinspection PyAttributeOutsideInit
            self._IP = True
        else:
            # noinspection PyAttributeOutsideInit
            self._IP = False

        _output_file = self.directory + "\\" + "organization.json"

        _outputs = dumps(self, indent=0, maintain_tuples=True)
        with open(_output_file, "w") as f:
            f.write(_outputs)
        f.close()

        print("Finished saving mouse.")

        if self._IP:
            # noinspection PyAttributeOutsideInit
            self._IP = get_ipython()

    # noinspection All
    def start_log(self) -> Self:
        """
        Starts Log

        :rtype: Any
        """
        self._IP = get_ipython()
        _magic_arguments = '-o -r -t ' + self.log_file + ' append'
        self._IP.run_line_magic('logstart', _magic_arguments)
        print("Logging Initiated")

    def update_all_folder_dictionaries(self) -> Self:
        """
        This function iterates through all behavioral ExperimentNames to update their folder dictionaries

        :rtype: Any
        """

        _update_keys = [_key for _key in dir(self) if isinstance(self.__getattribute__(_key), Experiment)]

        _pbar = tqdm(total=_update_keys.__len__())
        _pbar.set_description("Updating Folder Dictionaries")

        for _key in _update_keys:
            self.__dict__.get(_key).update_folder_dictionary()
            _pbar.update(1)

        _pbar.close()

    def _generate_experiment_folders(self, Name, **kwargs) -> None:
        """
        Generate Experiment ExperimentName Folder

        :param Name: Name of Experiment
        :type Name: str
        :keyword Behavior: Include Behavioral Folder (bool, default True)
        :keyword Imaging: Include Imaging Folder (bool, default True)
        :keyword Analysis: Include Analysis Folder (bool, default True)
        :rtype: None
        """


        _include_behavior = kwargs.get('Behavior', True)
        _include_imaging = kwargs.get('Imaging', True)
        _include_analysis = kwargs.get('Analysis', True)
        _include_figures = kwargs.get("Figures", True)
        _experiment_directory = "".join([self.directory, "\\", Name])

        if _include_behavior:
            self._generate_behavior_subdirectory(_experiment_directory)
        if _include_imaging:
            self._generate_imaging_subdirectory(_experiment_directory)
        if _include_analysis:
            self._generate_analysis_subdirectory(_experiment_directory)
        if _include_figures:
            self._generate_figures_subdirectory(_experiment_directory)

    @classmethod
    def load(cls, Directory: Optional[str] = None) -> Mouse:
        """
        Function that loads the entire mouse

        :param Directory: Directory containing the organization.json file and associated data
        :type Directory: Optional[str]
        :return: Mouse
        :rtype: ExperimentManagement.Organization.Mouse
        """
        if Directory is None:
            Directory = select_directory(title="Select folder containing mouse (organization.json)", mustexist=True)
        print("Loading Experiments...")
        _input_file = Directory + "\\organization.json"
        with open(_input_file, "r") as f:
            _data = loads(f.read())
        f.close()
        MouseData = Mouse()
        MouseData.__dict__.update(_data.__dict__)

        # convert ordered dicts to dicts
        _update_keys = [_key for _key in dir(MouseData) if isinstance(MouseData.__getattribute__(_key), Experiment)]
        for _key in _update_keys:
            if isinstance(MouseData.__dict__.get(_key).folder_dictionary, OrderedDict):
                MouseData.__dict__.get(_key).folder_dictionary = dict(MouseData.__dict__.get(_key).folder_dictionary)

        print("Finished.")
        if MouseData._log_file is not None:
            MouseData.start_log()
        return MouseData

    @classmethod
    def _generate_analysis_subdirectory(cls, ExperimentNameDirectory: str, **kwargs) -> None:
        """
        Generate Computation Folder

        Keyword Arguments
        -----------------
        *Title* : Computational Analysis Title (str, default AnalysisTechnique)

        :param ExperimentNameDirectory: Directory for folder creation
        :type ExperimentNameDirectory: str
        :keyword Title: Computational Analysis Title
        :rtype: None
        """
        _analysis_title = kwargs.get('Title', 'AnalysisTechnique')
        _base_comp_dir = ExperimentNameDirectory + "\\Analysis"
        _neural_data_dir = _base_comp_dir + "\\NeuralData"
        _analysis_dir = _base_comp_dir + "\\" + _analysis_title
        try:
            os.makedirs(_base_comp_dir)
        except FileExistsError:
            pass
        try:
            os.makedirs(_neural_data_dir)
        except FileExistsError:
            pass

    @classmethod
    def _generate_analysis_technique_subdirectory(cls, BaseCompDirectory: str, AnalysisTitle: str) -> None:
        """
        Generate Analysis Technique

        :param BaseCompDirectory: Base Directory for Computation
        :type BaseCompDirectory: str
        :param AnalysisTitle: Title for Analysis
        :type AnalysisTitle: str
        :rtype: None
        """
        _analysis_dir = BaseCompDirectory + "\\" + AnalysisTitle
        try:
            os.makedirs(_analysis_dir)
            generate_read_me(_analysis_dir + "\\ReadMe.txt", "Read-Me for Analysis Technique")
        except FileExistsError:
            pass

    @classmethod
    def _generate_behavior_subdirectory(cls, ExperimentNameDirectory: str) -> None:
        """
        Generate Behavioral Folder

        :param ExperimentNameDirectory: Directory for folder creation
        :type ExperimentNameDirectory: str
        :rtype: None
        """

        _base_behav_dir = ExperimentNameDirectory + "\\Behavior"
        _raw_behavioral_data = _base_behav_dir + "\\RawBehavioralData"
        _behavioral_exports = _base_behav_dir + "\\BehavioralExports"
        _deep_lab_cut_data = _base_behav_dir + "\\DeepLabCutData"
        try:
            os.makedirs(_base_behav_dir)
        except FileExistsError:
            pass
        try:
            os.makedirs(_raw_behavioral_data)
        except FileExistsError:
            pass
        try:
            os.makedirs(_behavioral_exports)
        except FileExistsError:
            pass
        try:
            os.makedirs(_deep_lab_cut_data)
        except FileExistsError:
            pass

    @classmethod
    def _generate_figures_subdirectory(cls, ExperimentNameDirectory: str) -> None:
        try:
            os.makedirs("".join([ExperimentNameDirectory, "\\Figures"]))
        except FileExistsError:
            pass

    @classmethod
    def _generate_histology_directory(cls, Directory: str, **kwargs) -> None:
        """
        Generates Histology Folder

        Keyword Arguments
        -----------------
        *Title* : Title of Histology Experiment (str, default None)

        :param Directory: Directory to generate folders in
        :type Directory: str
        :keyword Title: Title of Histology Experiment
        :rtype: None
        """

        _visual_hist_title = kwargs.get('Title', None)
        _base_hist_dir = Directory + "\\Histology"
        if _visual_hist_title is not None:
            _visual_hist_dir = _base_hist_dir + "\\" + _visual_hist_title
        else:
            _visual_hist_dir = _base_hist_dir + "\\Visualization"

        _read_me_file = _visual_hist_dir + "\\ReadMe.txt"

        try:
            os.makedirs(_base_hist_dir)
            os.makedirs(_visual_hist_dir)
        except FileExistsError:
            pass

        generate_read_me(_read_me_file, "Read-Me for Associated Histological Data")

    @classmethod
    def _generate_imaging_subdirectory(cls, ExperimentNameDirectory: str) -> None:
        """
        Generate Imaging Folder

        Keyword Arguments
        -----------------
        *SampleFrequency* : Image frequency (int, default 30)

        :param ExperimentNameDirectory: Directory for folder creation
        :type ExperimentNameDirectory: str
        :rtype: None
        """

        _base_image_dir = ExperimentNameDirectory + "\\Imaging"
        _raw_imaging_data = _base_image_dir + "\\RawImagingData"
        _bruker_meta_data = _base_image_dir + "\\BrukerMetaData"
        try:
            os.makedirs(_base_image_dir)
        except FileExistsError:
            pass
        try:
            os.makedirs(_raw_imaging_data)
        except FileExistsError:
            pass
        try:
            os.makedirs(_bruker_meta_data)
        except FileExistsError:
            pass

    @classmethod
    def _generate_roi_matching_index_directory(cls, Directory: str) -> None:
        """
        Generate ROI Matching Folder

        :rtype: None
        """
        _roi_matching_index_dir = Directory + "\\ROIMatchingIndex"
        _roi_matching_index_read_me = _roi_matching_index_dir + "\\ReadMe.txt"

        try:
            os.makedirs(_roi_matching_index_dir)
            generate_read_me(_roi_matching_index_read_me,
                            "Read-Me for Index of Longitudinally-Matched ROIs")
        except FileExistsError:
            pass


class Experiment:
    """
     Experiment class for a generic experiment

    **Required Inputs**
        | *Meta* : Passed meta from mouse (directory, mouse_id)
        | *ExperimentName* : Title of experiment

    **Properties**
        | *instance_data* : Identifies when this behavioral experiment was created
        | *mouse_id* : Identifies which mouse this data belongs to

    **Attributes**
        | *data* : a pandas dataframe containing synchronized data
        | *folder_dictionary* : A dictionary of relevant folders for this experiment
        | *modifications* : List of modifications made to this experiment

    **Public Methods**
        | *copy_data* : Interactive tool to copy data to directory (Intended to be overwritten during inheritance)
        | *load_data* : Loads all data (Intended to be overwritten during inheritance)
        | *record_mod* :  Records a modification made to the experiment (Date & Time)
        | *update_folder_dictionary* : This function re-indexes all folders in the folder dictionary

    """

    def __init__(self, Meta: Tuple[str, str], ExperimentName: str):
        # PROTECTED
        self.__mouse_id = Meta[1]
        self.__instance_date = get_date()
        self.__experiment_id = ExperimentName
        # PUBLIC
        self.data = None
        self.folder_dictionary = dict()
        self.modifications = [(get_date(), get_time())]
        _directory = Meta[0]
        self._create_folder_dictionary(_directory, ExperimentName)

    @property
    def instance_date(self) -> str:
        """
        Date created

        :rtype: str
        """
        return self._Experiment__instance_date

    @property
    def mouse_id(self) -> str:
        """
        ID of mouse

        :rtype: str
        """
        return self._Experiment__mouse_id

    @property
    def experiment_id(self) -> str:
        return self._Experiment__experiment_id

    def copy_data(self) -> Self:
        """
        Interactive tool to copy data to directory

        :rtype: Any
        """
        return

    def record_mod(self) -> Self:
        """
        Records a modification made to the behavioral ExperimentName (Date & Time)

        :rtype: Any
        """
        self.modifications.append((get_date(), get_time()))

    def update_folder_dictionary(self) -> Self:
        """
        This function re-indexes all folders in the folder dictionary

        :rtype: Any
        """

        # noinspection PyTypeChecker
        _update_keys = [_key for _key in self.folder_dictionary.keys()
                        if isinstance(self.folder_dictionary.get(_key), Data)]

        for _key in _update_keys:
            self.folder_dictionary.get(_key).reindex()

    def _create_folder_dictionary(self, Directory: str, ExperimentName: str) -> Self:
        """
        Creates a dictionary of locations for specific files

        :param Directory: Directory containing mouse data (passed meta)
        :type Directory: str
        :param ExperimentName: The ExperimentName ID
        :type ExperimentName: str
        :rtype: Any
        """
        _experiment_directory = Directory + "\\" + ExperimentName
        self.folder_dictionary = {
            'directory': Directory,
            'experiment_directory': _experiment_directory,
            'analysis_folder': _experiment_directory + "\\Analysis",
            'imaging_folder': _experiment_directory + "\\Imaging",
            'behavior_folder': _experiment_directory + "\\Behavior",
            "figures_folder": Figures("".join([_experiment_directory, "\\Figures"])),
        }


class ImagingExperiment(Experiment):
    """
    :class:`Experiment <Management.Organization.Experiment>` class for a generic imaging experiment

    **Required Inputs**
        | *Meta* : Passed meta from mouse  (directory, mouse_id)
        | *ExperimentName* : Title of experiment

    **Properties**
        | *mouse_id* : Identifies which mouse this data belongs to
        | *instance_data* : Identifies when this experiment was created

    **Attributes**
        | *data* : a pandas dataframe containing synchronized data
        | *folder_dictionary* : A dictionary of relevant folders for this experiment
        | *meta* : bruker metadata
        | *modifications* : List of modifications made to this experiment

    **Public Methods**
        | *add_image_sampling_folder* : Generates a folder for containing imaging data of a specific sampling rate
        | *copy_raw_imaging_data* : Interactive tool for copying raw imaging data
        | *load_data* : Loads all data
        | *record_mod* :  Records a modification made to the experiment (Date & Time)
        | *update_folder_dictionary* : This function re-indexes all folders in the folder dictionary

    """

    def __init__(self, Meta: Tuple[str, str], ExperimentName: str):
        """
        :param Meta: Passed Meta from experimental hierarchy
        :type Meta: tuple[str, str]
        :param ExperimentName: Title of ExperimentName
        :type ExperimentName: str
        """
        super().__init__(Meta, ExperimentName)

        self.meta = None
        self._fill_imaging_folder_dictionary()

    def _fill_imaging_folder_dictionary(self) -> Self:
        """
        Generates folders and a dictionary of imaging files (Raw, Meta, Compiled)

        :rtype: Any
        """
        # RAW
        _raw_data_folder = self.folder_dictionary['imaging_folder'] + "\\RawImagingData"
        try:
            os.makedirs(_raw_data_folder)
        except FileExistsError:
            pass
        self.folder_dictionary['raw_imaging_data'] = Images(_raw_data_folder)
        # META
        _bruker_meta_folder = self.folder_dictionary['imaging_folder'] + "\\BrukerMetaData"
        try:
            os.makedirs(_bruker_meta_folder)
        except FileExistsError:
            pass
        self.folder_dictionary['bruker_meta_data'] = Data(_bruker_meta_folder)

    def _load_bruker_analog_recordings(self) -> pd.DataFrame:
        """
        Loads Bruker Analog Recordings

        :returns: Analog Recording
        :rtype: pd.DataFrame
        """

        self.folder_dictionary["bruker_meta_data"].reindex()
        _files = self.folder_dictionary["bruker_meta_data"].find_all_ext("csv")
        return self._load_bruker_analog_file(_files[-1])

    def _load_bruker_meta_data(self) -> Self:
        """
        Loads Bruker Meta Data

        :rtype: Any
        """
        self.folder_dictionary["bruker_meta_data"].reindex()
        _files = self.folder_dictionary["bruker_meta_data"].find_all_ext("xml")
        _files = [_files[0], _files[2], _files[1]]
        # Rearrange as Imaging, Voltage Recording, Voltage Output
        self.meta = self._load_bruker_meta_file(_files)

    def add_image_sampling_folder(self, SamplingRate: int) -> Self:
        """
        Generates a folder for containing imaging data of a specific sampling rate

        :param SamplingRate: Sampling Rate of Dataset in Hz
        :type SamplingRate: int
        :rtype: Any
        """
        SamplingRate = str(SamplingRate)  # Because we know I'll always forget and send an int anyway
        _folder_name = "".join([self.folder_dictionary['imaging_folder'], "\\", SamplingRate, "Hz"])
        _key_name = "".join(["imaging_", SamplingRate, "Hz"])
        try:
            os.makedirs(_folder_name)
        except FileExistsError:
            print("The sampling folder already exists. Adding to folder dictionary")
        # setattr(self, _attr_name, ImagingAnalysis(_folder_name)) changing to be in folder dictionary
        self.folder_dictionary[_key_name] = ImagingAnalysis(_folder_name)
        self._generate_imaging_sampling_rate_subdirectory(_folder_name)
        self.update_folder_dictionary()

    def copy_data(self) -> Self:
        self.copy_raw_imaging_data()

    def copy_raw_imaging_data(self) -> Self:
        """
        This function copies raw imaging data to the appropriate folder

        :rtype: Any
        """

        _raw_imaging_data_path = select_directory(title="Select folder containing raw imaging data", mustexist=True)
        verbose_copying(_raw_imaging_data_path, self.folder_dictionary.get("raw_imaging_data").path)

    def load_data(self, ImagingParameters: Optional[Union[dict, list[dict]]] = None) -> Self:
        """
        Loads all data

        :param ImagingParameters: Parameters for some imaging dataset or list of datasets (e.g., for two different sampling rates)
        :type ImagingParameters: Optional[dict]
        :rtype: Any
        """
        # Load Behavior
        if self.data is not None:
            input("\nDetected there is currently data loaded!\n Would you like to Overwrite?(Y/N)\n")
            if input == "Y" or input == "Yes" or input == "Ye" or input == "es":
                pass
            else:
                return

        # Load Imaging Meta
        if ImagingParameters is not None:
            self._load_bruker_meta_data()

    @classmethod
    def _generate_imaging_sampling_rate_subdirectory(cls, SampFreqDirectory: str) -> None:
        """
        Generate Sample Frequency Folder Innards

        :param SampFreqDirectory: Directory for folder creation
        :type SampFreqDirectory: str
        :rtype: None
        """
        _suite2p = SampFreqDirectory + "\\suite2p"
        _fissa = SampFreqDirectory + "\\fissa"
        _roi_sorting = SampFreqDirectory + "\\sorting"
        _denoised = SampFreqDirectory + "\\denoised"
        _cascade = SampFreqDirectory + "\\cascade"
        _compiled = SampFreqDirectory + "\\compiled"
        os.makedirs(_suite2p)
        os.makedirs(_fissa)
        os.makedirs(_denoised)
        os.makedirs(_roi_sorting)
        os.makedirs(_cascade)
        os.makedirs(_compiled)
        generate_read_me(_roi_sorting + "\\ReadMe.txt", "Read-Me for ROI Sorting")

    @staticmethod
    def _load_bruker_analog_file(File: str) -> pd.DataFrame:
        """
        Method to load bruker analog recordings from .csv

        :param File: filepath
        :type File: str
        :return: analog recordings
        :rtype: pd.DataFrame
        """
        assert(pathlib.Path(File).suffix == ".csv")
        return pd.read_csv(File)

    @staticmethod
    def _load_bruker_meta_file(File: Union[str, list[str]]) -> BrukerMeta:
        """
        Loads bruker meta file using a class wrapping sam's code

        :param File: Filename of a single or list of bruker meta files
        :type File: Union[str, list[str]]
        :return: the metadata
        :rtype: BrukerMeta
        """
        if isinstance(File, list):
            meta = BrukerMeta(*File)
        else:
            meta = BrukerMeta(File)

        meta.import_meta_data()

        meta.creation_date = get_date()

        return meta


class BehavioralExperiment(Experiment):
    """
    :class:`Experiment <Management.Organization.Experiment>` class for a generic day of a behavioral task

    **Required Inputs**
        | *Meta* : Passed meta from experimental hierarchy (directory, mouse_id)
        | *ExperimentName* : Title of ExperimentName

    **Properties**
        | *mouse_id* : Identifies which mouse this data belongs to
        | *instance_data* : Identifies when this behavioral ExperimentName was created

    **Attributes**
        | *data* : Pandas dataframe of synced data
        | *folder_dictionary* : A dictionary of relevant folders for this behavioral ExperimentName
        | *modifications* : List of modifications made to this behavioral ExperimentName
        | *multi_index*: Pandas multi-index of behavioral components
        | *state_index* : look-up table / index relating states to integers
        | *trial_parameters* : behavioral parameters

    **Methods**
        | *copy_raw_behavioral_data* : Interactive tool for copying raw behavioral data
        | *load_data* : Loads all data
        | *record_mod* :  Records a modification made to the behavioral ExperimentName (Date & Time)
        | *update_folder_dictionary* : This function re-indexes all folders in the folder dictionary
    """

    def __init__(self, Meta: Tuple[str, str], ExperimentName: str):
        """
        :param Meta: Passed Meta from experimental hierarchy
        :type Meta: tuple[str, str]
        :param ExperimentName: Title of ExperimentName
        :type ExperimentName: str
        """
        super().__init__(Meta, ExperimentName)

        # PUBLIC
        self.multi_index = None
        self.state_index = dict()
        self.trial_parameters = dict()

    def load_data(self) -> Self:
        """
         Loads behavioral data

        :rtype: Any
        """

        # Load Behavior
        if self.data is not None:
            input("\nDetected there is currently data loaded!\n Would you like to Overwrite?(Y/N)\n")
            if input == "Y" or input == "Yes" or input == "Ye" or input == "es":
                pass
            else:
                return

        self._load_base_behavior()

    def copy_raw_behavioral_data(self) -> Self:
        """
        Interactive tool for copying raw behavioral data

        :rtype: Any
        """

        raw_behavioral_data_path = select_directory(title="Select folder containing raw behavioral data", mustexist=True)
        verbose_copying(_raw_imaging_data_path, self.folder_dictionary.get("raw_behavioral_data").path)

    def _load_base_behavior(self) -> Self:
        """
        Loads the basic behavioral data: analog, dictionary, digital, state, and CS identities

        :rtype: Any
        """

        print("Loading Base Data...")
        # Analog
        _analog_file = "".join([self.folder_dictionary.get("behavior_folder"), "\\analog.npy"])
        _analog_data = np.load(_analog_file, allow_pickle=True)

        # Digital
        _digital_file = "".join([self.folder_dictionary.get("behavior_folder"), "\\digital.npy"])
        _digital_data = np.load(_digital_file, allow_pickle=True)

        # State
        _state_file = "".join([self.folder_dictionary.get("behavior_folder"), "\\state_data.npy"])
        _state_data = np.load(_state_file, allow_pickle=True
                              )
        # Dictionary
        _dictionary_file = "".join([self.folder_dictionary.get("behavior_folder"), "\\config.npy"])
        with open(_dictionary_file, "rb") as f:
            _dictionary_data = pkl.load(f)

        try:
            self.trial_parameters = _dictionary_data.copy()  # For Safety
        except AttributeError:
            print(_dictionary_data)

        # Form Pandas DataFrame
        self.data, self.state_index, self.multi_index = self._organize_base_data(_analog_data, _digital_data,
                                                                                 _state_data)

    @staticmethod
    def _organize_base_data(Analog: np.ndarray, Digital: np.ndarray, State: np.ndarray,
                            HardwareConfig: Optional[dict] = None) -> pd.DataFrame:
        """
        This function organizes analog, digital, and state data into a pandas dataframe

        :param Analog: Analog Data
        :type Analog: Any
        :param Digital: Digital Data
        :type Digital: Any
        :param State: State Data
        :type State: Any
        :param HardwareConfig: Dictionary indicating configuration of hardware channels
        :type HardwareConfig: dict
        :return: Data organized into a pandas dataframe
        :rtype: pd.DataFrame
        """

        # Parse Channel IDs
        if HardwareConfig is None:
            _analog_dictionary = {
                "Imaging Sync": 0,
                "Motor Position": 1,
                "Force": 3,
            }
            _digital_dictionary = {
                "Gate": 0
            }
        else:
            print("Not yet implemented, reverting to defaults")
            _analog_dictionary = {
                "Imaging Sync": 0,
                "Motor Position": 1,
                "Force": 3,
            }
            _digital_dictionary = {
                "Gate": 0
            }

        # Determine Sampling Rates
        if HardwareConfig is None:
            _data_sampling_rate = 1000
            _state_sampling_rate = 10
        else:
            print("Not yet implemented, reverting to defaults")
            _data_sampling_rate = 1000
            _state_sampling_rate = 10

        def nest_all_ExperimentNames_under_trials(State_Data: np.ndarray, Index: np.ndarray, State_Casted_Dict: dict) \
                -> pd.Series:
            nested_trial_index = np.full(Index.__len__(), 6969, dtype=np.float64)
            _trial_idx = np.where(State_Data == State_Casted_Dict.get("Trial"))[0]
            _deriv_idx = np.diff(_trial_idx)
            _trailing_edge = _trial_idx[np.where(_deriv_idx > 1)[0]]
            _trailing_edge = np.append(_trailing_edge, _trial_idx[-1])
            _habituation_trailing_edge = np.where(State_Data == State_Casted_Dict.get("Habituation"))[0][-1]

            nested_trial_index[_habituation_trailing_edge] = -1
            nested_trial_index[-1] = _trailing_edge.__len__()

            for _edge in range(_trailing_edge.shape[0]):
                nested_trial_index[_trailing_edge[_edge]] = _edge

            nested_trial_index = pd.Series(nested_trial_index, index=Index, dtype=np.float64)
            nested_trial_index[nested_trial_index == 6969] = np.nan
            nested_trial_index.bfill(inplace=True)
            nested_trial_index.name = "Trial Set"
            return nested_trial_index

        def construct_state_index_series(State_Data: np.ndarray, Time_Vector_Data: np.ndarray,
                                         Time_Vector_State: np.ndarray) -> Tuple[dict, pd.Series]:
            def cast_state_into_float64(State__Data: np.ndarray) -> Tuple[np.ndarray, dict]:
                State__Casted__Dict = dict()
                Integer_State_Index = np.full(State__Data.shape[0], 0, dtype=np.float64)
                _unique_states = np.unique(State__Data)

                for _unique_value in range(_unique_states.shape[0]):
                    State__Casted__Dict[_unique_states[_unique_value]] = _unique_value
                    Integer_State_Index[np.where(State__Data == _unique_states[_unique_value])[0]] = _unique_value

                return Integer_State_Index, State__Casted__Dict

            _integer_state_index, State_Casted_Dict = cast_state_into_float64(State_Data)
            State_Index = pd.Series(_integer_state_index, index=Time_Vector_State)
            State_Index.sort_index(inplace=True)
            State_Index = State_Index.reindex(Time_Vector_Data)
            State_Index.ffill(inplace=True)
            State_Index.name = "State Integer"
            return State_Casted_Dict, State_Index

        # Create Time Vectors
        _time_vector_data = np.around(np.arange(0, Analog.shape[1] * (1 / _data_sampling_rate), 1 / _data_sampling_rate,
                                                dtype=np.float64),
                                      decimals=3)
        _time_vector_state = np.around(np.arange(0, State.__len__() * (1 / _state_sampling_rate), 1 /
                                                 _state_sampling_rate, dtype=np.float64), decimals=3)

        # Construct State Index
        StateCastedDict, _state_index = construct_state_index_series(State, _time_vector_data, _time_vector_state)

        # Construct Nested Trial Index
        _trial_index = nest_all_ExperimentNames_under_trials(_state_index.to_numpy(), _time_vector_data, StateCastedDict)

        # Create Multi-Index
        MultiIndex = pd.MultiIndex.from_arrays([_state_index.to_numpy(), _trial_index.to_numpy(), _time_vector_data])
        MultiIndex.names = ["State Integer", "Trial Set", "Time (s)"]

        # Initialize Organized Data Frame
        OrganizedData = pd.DataFrame(None, index=_time_vector_data, dtype=np.float64)
        OrganizedData.index.name = "Time (s)"

        # Type Check
        try:
            assert (_state_index.to_numpy().dtype == np.float64)
            assert (_trial_index.to_numpy().dtype == np.float64)
            assert (Analog.dtype == np.float64)
            assert (Digital.dtype == np.float64)
        except AssertionError:
            print("Bug. Incorrect Type detected. Forcing conversion...")
            try:
                _state_index.to_numpy().astype(np.float64)
                _trial_index.to_numpy().astype(np.float64)
                Analog.astype(np.float64)
                Digital.astype(np.float64)
                print("Successfully converted erroneous data types")
            except AttributeError:
                print("Failed automatic conversion")
                return OrganizedData

        # Add According to Index, Start with State Integer
        OrganizedData = OrganizedData.join(_state_index, on="Time (s)")
        OrganizedData = OrganizedData.join(_trial_index, on="Time (s)")

        # Add Analogs
        if Analog.shape[0] < Analog.shape[1]:  # orientation check
            Analog = Analog.T

        for _key in _analog_dictionary:
            _analog_series = pd.Series(Analog[:, _analog_dictionary.get(_key)], index=_time_vector_data,
                                       dtype=np.float64)
            _analog_series.name = _key
            OrganizedData = OrganizedData.join(_analog_series, on="Time (s)")

        # Add Digital
        if _digital_dictionary.keys().__len__() > 1:
            for _key in _digital_dictionary:
                _digital_series = pd.Series(Digital[:, _digital_dictionary.get(_key)], index=_time_vector_data,
                                            dtype=np.float64)
                _digital_series.name = _digital_dictionary.get(_key)
                OrganizedData = OrganizedData.join(_digital_series, on="Time (s)")
        else:
            _digital_series = pd.Series(Digital, index=_time_vector_data, dtype=np.float64)
            _digital_series.name = list(_digital_dictionary.keys())[0]
            OrganizedData = OrganizedData.join(_digital_series, on="Time (s)")

        # sort alphabetically for ease of viewing/debugging
        OrganizedData = OrganizedData.reindex(columns=sorted(OrganizedData.columns))

        return OrganizedData, StateCastedDict, MultiIndex


class ImagingBehaviorExperiment(ImagingExperiment, BehavioralExperiment):
    """
    :class:`Experiment <Management.Organization.Experiment>` class for a generic day of an
    :class:`Imaging <Management.Organization.ImagingExperiment>` /
    :class:`Behavioral <Management.Organization.BehavioralExperiment>` experiment

    **Required Inputs**
        | *Meta* : Passed meta from experimental hierarchy (directory, mouse_id)
        | *ExperimentName* : Title of ExperimentName

    **Properties**
        | *mouse_id* : Identifies which mouse this data belongs to
        | *instance_data* : Identifies when this behavioral ExperimentName was created

    **Attributes**
        | *data* : Pandas dataframe of synced data
        | *folder_dictionary* : A dictionary of relevant folders for this behavioral ExperimentName
        | *modifications* : List of modifications made to this behavioral ExperimentName
        | *meta* : bruker metadata
        | *multi_index*: Pandas multi-index of behavioral components
        | *state_index* : look-up table / index relating states to integers
        | *trial_parameters* : behavioral parameters

    **Methods**
        | *copy_raw_imaging_data* : Interactive tool for copying raw imaging data
        | *copy_raw_behavioral_data* : Interactive tool for copying raw behavioral data
        | *load_data* : Loads all data
        | *record_mod* :  Records a modification made to the experiment (Date & Time)
        | *update_folder_dictionary* : This function re-indexes all folders in the folder dictionary

    """

    def __init__(self, Meta: Tuple[str, str], ExperimentName: str):
        """
        :param Meta: Passed Meta from experimental hierarchy
        :type Meta: tuple[str, str]
        :param ExperimentName: Title of ExperimentName
        :type ExperimentName: str
        """
        super().__init__(Meta, ExperimentName)

    def load_data(self, ImagingParameters: Optional[Union[dict, list[dict]]] = None,
                  *args: Optional[Tuple[str, str]], **kwargs) -> Self:
        """
         Loads all data

        :param ImagingParameters: Parameters for some imaging dataset or list of datasets
        (e.g., for two different sampling rates)
        :type ImagingParameters: Optional[dict]
        :param args: Optionally pass Sync Key to synchronize bruker recordings
        :type args: Tuple[str, str]
        :param kwargs: passed to internal functions taking kwargs
        :rtype: Any
        """
        # Load Behavior
        if self.data is not None:
            input("\nDetected there is currently data loaded!\n Would you like to Overwrite?(Y/N)\n")
            if input == "Y" or input == "Yes" or input == "Ye" or input == "es":
                pass
            else:
                return

        self._load_base_behavior()

        # Load Imaging Meta
        if ImagingParameters is not None:
            self._load_bruker_meta_data()

        # Sync Imaging Data
        if args and ImagingParameters is not None:
            if isinstance(ImagingParameters, dict):
                self.data = self._sync_bruker_recordings(self.data, self._load_bruker_analog_recordings(), self.meta,
                                                         self.state_index, *args, ImagingParameters)
                if ImagingParameters.get(("preprocessing", "grouped-z project bin size")):
                    self.data = self._sync_grouped_z_projected_images(self.data, self.meta, ImagingParameters)
            elif isinstance(ImagingParameters, list) and isinstance(ImagingParameters[-1], dict):
                self.data = self._sync_bruker_recordings(self.data, self._load_bruker_analog_recordings(), self.meta,
                                                         self.state_index, *args, ImagingParameters[0])
                for _sampling in range(1, ImagingParameters.__len__(), 1):
                    self.data = self._sync_grouped_z_projected_images(
                        self.data, self.meta, ImagingParameters[_sampling],
                        "".join(["Down-sampled Imaging Frame Set ", str(_sampling)]))

    def copy_data(self) -> Self:
        self.copy_raw_imaging_data()
        self.copy_raw_behavioral_data()

    @staticmethod
    def _sync_bruker_recordings(DataFrame: pd.DataFrame, AnalogRecordings: pd.DataFrame, MetaData: BrukerMeta,
                                StateCastedDict: dict,
                                SyncKey: Tuple[str, str], Parameters: dict, **kwargs) -> pd.DataFrame:
        """

        :param DataFrame:
        :type DataFrame: pd.DataFrame
        :param AnalogRecordings:
        :type AnalogRecordings: pd.DataFrame
        :param MetaData:
        :type MetaData: BrukerMeta
        :param StateCastedDict:
        :type StateCastedDict: dict
        :param SyncKey:
        :type SyncKey: tuple or None
        :param Parameters: dictionary containing preprocessing and other parameters
        :type Parameters: dict
        :return: Sync Data
        :rtype: pd.DataFrame
        """

        _fill_method = kwargs.get("fill", "nearest")
        # Sync by matching first peak of the sync_key columns
        _DF_signal = DataFrame[SyncKey[0]].to_numpy().copy()
        _AR_signal = AnalogRecordings[SyncKey[1]].to_numpy().copy()
        _AR_first_peak = np.where(np.diff(_AR_signal) > 1.0)[0][0] + 1
        assert (_AR_signal[_AR_first_peak] >= 3.3)

        _first_peak_diff = np.where(_DF_signal == StateCastedDict.get("Trial"))[0][0] - _AR_first_peak

        if _first_peak_diff > 0:
            print("NOT YET IMPLEMENTED")
            # noinspection PyTypeChecker
            return
            # noinspection PyUnreachableCode
            _AR_signal = np.pad(_AR_signal, (_first_peak_diff, 0), constant_values=0)
        elif _first_peak_diff < 0:
            _first_peak_diff *= -1
            _AR_signal = pd.DataFrame(AnalogRecordings.iloc[_first_peak_diff:, 1:].to_numpy(),
                                      index=np.around(
                                          (AnalogRecordings.index.to_numpy()[
                                           _first_peak_diff:] - _first_peak_diff) /
                                          int(MetaData.acquisition_rate), decimals=3) + DataFrame.index.to_numpy()[
                                                0])
            _AR_signal.columns = AnalogRecordings.columns[1:]

            _frames = pd.Series(np.arange(0, MetaData.imaging_metadata.get("relativeTimes").__len__(), 1),
                                index=np.around(MetaData.imaging_metadata.get("relativeTimes") -
                                                AnalogRecordings["Time(ms)"].to_numpy()[_first_peak_diff] / int(
                                    MetaData.acquisition_rate), decimals=3) + DataFrame.index.to_numpy()[0])
            _frames = _frames[_frames.index >= 0 + DataFrame.index.to_numpy()[0]].copy(deep=True)
            _frames.name = "Imaging Frame"
        else:
            print("Already Synced")

        # Here I just make sure shape-match
        if _DF_signal.shape[0] < _AR_signal.shape[0]:
            _AR_signal = _AR_signal.iloc[0:_DF_signal.shape[0], :]
            _frames = _frames[_frames.index <= DataFrame.index.to_numpy()[-1]].copy(deep=True)
            print("Cropped Bruker Signals")
        elif _DF_signal.shape[0] > _AR_signal.shape[0]:
            # _AR_signal.to_numpy() = np.pad(_AR_signal.to_numpy(), pad_width=((0, _DF_signal.shape[0] - _AR_signal.shape[0]), (0, 0)),
            # mode="constant", constant_values=0)

            _AR_signal = _AR_signal.reindex(DataFrame.index)
            # _frames = _frames.reindex(DataFrame.index) no need, happens below anyway

        # Merge/Export Analog
        # DataFrame = DataFrame.join(_AR_signal.copy(deep=True))
        DataFrame = DataFrame.join(_AR_signal)

        # Merge/Export Images
        DataFrame = DataFrame.join(_frames.copy(deep=True))
        # na filling column
        _frames = pd.DataFrame(_frames).copy(deep=True)
        _frames = _frames.reindex(DataFrame.index)
        if _fill_method == "backward":
            _frames.bfill(inplace=True)
        elif _fill_method == "forward":
            _frames.ffill(inplace=True)
        elif _fill_method == "nearest":
            _frames.interpolate(method="nearest", inplace=True)
        _frames = _frames.rename(columns={"Imaging Frame": "[FILLED] Imaging Frame"})

        DataFrame = DataFrame.join(_frames.copy(deep=True))

        # adjust for preprocessing
        # parse params
        _artifact = Parameters.get(("preprocessing", "shuttle artifact length"), 1000)
        _chunk_size = Parameters.get(("preprocessing", "chunk size"), 7000)

        # parse meta
        _num_frames = MetaData.imaging_metadata.get("relativeTimes").__len__()

        # determine original frames
        if _num_frames % _chunk_size >= _artifact:
            _first_frame = _num_frames % _chunk_size
        else:
            _artifact_free_frames = _num_frames - _artifact
            _additional_crop = _artifact_free_frames % _chunk_size
            _first_frame = _additional_crop + _artifact

        # sort alphabetically for ease of viewing/debugging
        DataFrame = DataFrame.reindex(columns=sorted(DataFrame.columns))

        return DataFrame

    @staticmethod
    def _sync_grouped_z_projected_images(DataFrame: pd.DataFrame, MetaData: BrukerMeta, Parameters: dict,
                                         *args: str) -> \
            pd.DataFrame:
        print("\nSyncing Images...")

        if args:
            _name = args[0]
        else:
            _name = "Downsampled Imaging Frame"

        # parse params
        _bin_size = Parameters.get(("preprocessing", "grouped-z project bin size"))
        _artifact = Parameters.get(("preprocessing", "shuttle artifact length"))
        _chunk_size = Parameters.get(("preprocessing", "chunk size"))

        # parse meta
        _num_frames = MetaData.imaging_metadata.get("relativeTimes").__len__()

        # determine downsample frames
        _original_downsample_frames = np.arange(0, _num_frames, 3).__len__()
        if _original_downsample_frames % _chunk_size >= _artifact:
            _first_downsample_frame = _original_downsample_frames % _chunk_size
        else:
            _artifact_free_downsample_frames = _original_downsample_frames - _artifact
            _additional_crop_downsample = _artifact_free_downsample_frames % _chunk_size
            _first_downsample_frame = _artifact_free_downsample_frames + _additional_crop_downsample
        _projected_frames = np.arange(_first_downsample_frame, _num_frames, 3)
        _projected_first_frame = _projected_frames[0] * 3
        _matching_frames = np.arange(_projected_first_frame, _num_frames, 3) + 1
        # make the center frame the timestamp instead of the first frame
        _time_stamp = np.full(_matching_frames.shape, -1, dtype=np.float64)
        for _frame in range(_matching_frames.__len__()):
            try:
                _time_stamp[_frame] = DataFrame.index.to_numpy()[
                    np.where(DataFrame["Imaging Frame"].to_numpy() == _matching_frames[_frame])[0]]
            except ValueError:
                pass
        _true_idx = np.where(_time_stamp != -1)[0]
        _time_stamp = _time_stamp[np.where(_time_stamp != -1)[0]]

        _downsampled_frames = pd.Series(np.arange(0, _time_stamp.shape[0], 1),
                                        index=_time_stamp)
        _downsampled_frames.name = _name

        DataFrame = DataFrame.join(_downsampled_frames.copy(deep=True), on="Time (s)")

        _downsampled_frames.reindex(DataFrame.index)
        _downsampled_frames.name = "".join(["[FILLED] ", _name])
        _downsampled_frames.interpolate(method="nearest", inplace=True)
        DataFrame = DataFrame.join(_downsampled_frames, on="Time (s)")

        DataFrame = DataFrame.reindex(columns=sorted(DataFrame.columns))

        print("\nFinished.")
        return DataFrame


class Data:
    """
    This is a class for managing a folder of unorganized data files

    **Required Inputs**
        | *Path* : absolute filepath for data folder

    **Self Methods**
        | *find_all_ext* :  Finds all files with specific extension
        | *find_matching_files* : Finds all matching files
        | *reindex* : Function that indexed the files within folder again

    **Properties**
        | *files* : List of files in folder
        | *instance_data* : Data created
        | *path* : path to folder

    """

    def __init__(self, Path: str):
        # Protected In Practice
        self.__instance_date = get_date()
        self._path = str()
        self._path_assigned = False

        # Properties
        self._folders = []
        self._files = []
        self.path = Path
        self.files = self.path
        self.folders = self.path

    @property
    def files(self) -> List[str]:
        return self._files

    @files.setter
    def files(self, Path: str) -> Self:
        """
       function to quickly fill recursively

        :param Path: Directory to check
        :type Path: str
        :rtype: Any
        """

        self._files = [_file for _file in pathlib.Path(Path).rglob("*") if _file.is_file()]

    @property
    def folders(self) -> dict:
        """
        Dictionary of folders in path

        :rtype: dict
        """
        return self._folders

    @folders.setter
    def folders(self, Path: str) -> Self:
        """
        function to quickly fill folders recursively

        :param Path: Directory to check
        :type Path: str
        :rtype: Any
        """
        _folders_list = [_folder for _folder in pathlib.Path(Path).rglob("*") if not _folder.is_file()]
        self._folders = dict() # Reset
        for _folder in _folders_list:
            self._folders[_folder.stem] = str(_folder)

    @property
    def instance_date(self) -> str:
        """
        Date Created

        :rtype: str
        """
        return self._Data__instance_date

    @property
    def path(self) -> str:
        """
        Path to folder

        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, Path: str) -> Self:
        if self._path_assigned is False:
            self._path = Path
            self._path_assigned = True
        else:
            print("Path can only be assigned ONCE.")

    def find_all_ext(self, Ext: str) -> Union[List[str], None]:
        """
        Finds all files with specific extension

        :param Ext: Filename extension
        :type Ext: str
        :return: List of files
        :rtype: List[str]
        """
        # make sure appropriately formatted

        if "." not in Ext:
            Ext = "".join([".", Ext])

        if "*" in Ext:
            ext.replace("*", "")

        self.reindex() # reindex to be sure not missing anything

        return [str(file) for file in self.files if file.suffix == Ext]

    def find_matching_files(self, Filename: str, Folder: Optional[str] = None) -> Union[Tuple[str], None]:
        """
        Finds all matching files

        :param Filename: Filename or  ID to search for
        :type Filename: str
        :param Folder: Specify folder filename in
        :type Folder: Any
        :return: Matching file/s
        :rtype: Any
        """
        # arg for specifying folder

        self.reindex() # reindex to be sure not missing anything

        if Folder is not None:
            Filename = "".join([Folder, "\\", Filename])

        return [str(_path) for _path in self.files if Filename in str(_path)]

    def reindex(self) -> Self:
        """
        Function that indexes the files within folder again
        """

        self.files = self.path
        self.folders = self.path


class Images(Data):
    """
    :class:`Data Folder <Management.Organization.Data>` specifically for folders containing raw images.

    **Required Inputs**
        | *Path* : absolute filepath for data folder

    """

    def __init__(self, Path: str):
        super().__init__(Path)

    def reorganize_bruker_files(self) -> None:
        """
        This function extracts out the meta files and saves in a new directory

        :rtype: None
        """

        _parent_directory = pathlib.Path(self.path).parents[0]
        _bruker_meta_folder = "".join([str(_parent_directory), "\\", "BrukerMetaData"])

        try:
            os.mkdir(_bruker_meta_folder)
        except FileExistsError:
            pass

        try:
            _reference_folder = pathlib.Path(self.folders.get("References"))
            _files = [_file for _file in _reference_folder.rglob("*") if _file.is_file()]
            for _file in _files:
                _file.rename("".join([_bruker_meta_folder, "\\", _file.name]))

            # Only remove folder if nothing left!!!
            if [_folder for _folder in _reference_folder.rglob("*") if not _folder.is_file()].__len__() == 0:
                _reference_folder.rmdir()

        except FileNotFoundError:
            print("Could not locate a bruker reference folder")

        for _meta_file in self.meta_files:
            _meta_file.rename("".join([_bruker_meta_folder, "\\", _meta_file.name]))

        for _file in self.find_all_ext(".csv"):
            pathlib.Path(_file).rename("".join([_bruker_meta_folder, "\\", pathlib.Path(_file).name]))

        if self.planes > 1 and self.channels == 1:
            for _plane in range(self.planes):
                _plane_folder = "".join([_parent_directory, "\\", "raw_imaging_data_plane_", str(_plane)])
                try:
                    os.mkdir(_plane_folder)
                except FileExistsError:
                    pass

    @property
    def file_format(self):
        # Needs modified for edge cases !!!!
        if self.files.__len__() != 0:
            _exts = [file.suffix for file in self.files]
            _counts = np.array([_exts.count(ext) for ext in np.unique(_exts)])
            return np.unique(_exts)[np.where(_counts == np.max(_counts))[0]][0]
        else:
            return "No files detected"

    @property
    def num_imaging_files(self):
        if self.files.__len__() != 0:
            return self.imaging_files.__len__()
        else:
            return 0

    @property
    def imaging_files(self):
        _file_format = self.file_format
        return [file for file in self.files if file.suffix == _file_format]

    @property
    def meta_files(self):
        if self.files.__len__() != 0:
            _exts = [file.suffix for file in self.files]
            return [file for file in self.files if file.suffix in [".xml", ".txt", ".env"]]
        else:
            return 0

    @property
    def num_meta_files(self):
        if self.files.__len__() != 0:
            return self.meta_files.__len__()
        else:
            return 0

    @property
    def planes(self):
        return determine_bruker_folder_contents(self.path)[1]

    @property
    def channels(self):
        return determine_bruker_folder_contents(self.path)[0]

    @property
    def frames(self):
        return determine_bruker_folder_contents(self.path)[2]

    @property
    def width(self):
        return determine_bruker_folder_contents(self.path)[4]

    @property
    def height(self):
        return determine_bruker_folder_contents(self.path)[3]


class Figures(Data):
    """
    :class:`Data Folder <Management.Organization.Data>` specifically for storing figures.

    **Required Inputs**
        | *Path* : absolute filepath for data folder
    """

    def __init__(self, Path: str):
        super().__init__(Path)


    def view_figure(self, Name: str) -> plt.Figure:
        """ Function identifies and views a figure based on supplied name

        :param Name: Name of figure (can be partial)
        :type Name: str

        :return: the plotted figure
        :rtype: Any
        """

        _filename = self.find_matching_files(Name)[0]
        return plt.imread(_filename)


def generate_read_me(AbsoluteFilePath: str, Text: str) -> None:
    """
    Generate a read me file

    :param AbsoluteFilePath: Filename path
    :type AbsoluteFilePath: str
    :param Text: Text inside
    :type Text: str
    :rtype: None
    """
    with open(AbsoluteFilePath, 'w') as _read_me:
        _read_me.write(Text)
        _read_me.close()


def get_date():
    return date.isoformat(date.today())


def get_time():
    return datetime.now().strftime("%H:%M:%S")
