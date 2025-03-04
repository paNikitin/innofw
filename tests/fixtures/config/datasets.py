# third party libraries
from omegaconf import DictConfig

from tests.utils import get_test_folder_path

# local modules

lep_datamodule_cfg_w_target = DictConfig(
    {
        "task": ["image-detection"],
        "name": "lep",
        "description": "object detection dataset of lep",
        "markup_info": "Информация о разметке",
        "date_time": "01.07.2076",
        "_target_": "innofw.core.integrations.UltralyticsDataModule",
        "train": {
            "source": str(
                get_test_folder_path() / "data/images/detection/lep/images/train"
            )
        },
        "test": {
            "source": str(
                get_test_folder_path() / "data/images/detection/lep/images/test"
            )
        },
        "infer": {
            "source": str(
                get_test_folder_path() / "data/images/detection/lep/images/infer"
            )
        },
        "num_workers": 8,
        "val_size": 0.2,
        "image_size": 128,
        "num_classes": 4,
        "batch_size": 2,
        "names": ["lep_1", "lep_2", "lep_3", "lep_4"],
    }
)

# remote_lep_datamodule_cfg_w_target = DictConfig(
#     {
#         "task": ["image-detection"],
#         "name": "lep",
#         "description": "object detection dataset of lep",
#         "markup_info": "Информация о разметке",
#         "date_time": "01.07.2076",
#         "_target_": "innofw.datamodules.lightning_datamodules.detection.YOLOv5DataModule",
#         "train": {
#             "source": str(
#                 get_test_folder_path() / "data/images/detection/lep/train"
#             )
#         },
#         "test": {
#             "source": str(
#                 get_test_folder_path() / "data/images/detection/lep/test"
#             )
#         },
#         "num_workers": 8,
#         "val_size": 0.2,
#         "image_size": 128,
#         "num_classes": 4,
#         "names": ["lep_1", "lep_2", "lep_3", "lep_4"],
#     }
# )

house_prices_datamodule_cfg_w_target = DictConfig(
    {
        "task": ["table-regression"],
        "name": "house prices",
        "description": "",
        "markup_info": "",
        "date_time": "01.07.2022",
        "_target_": "innofw.core.datamodules.pandas_datamodules.PandasDataModule",
        "train": {
            "source": str(
                get_test_folder_path()
                / "data/tabular/regression/house_prices/train/train.csv"
            )
        },
        "test": {
            "source": str(
                get_test_folder_path()
                / "data/tabular/regression/house_prices/test/test.csv"
            )
        },
        "target_col": "price",
    }
)

wheat_datamodule_cfg_w_target = DictConfig(
    {
        "task": ["image-detection"],
        "name": "wheat",
        "description": "object detection dataset of wheat",
        "markup_info": "Информация о разметке",
        "date_time": "01.07.2076",
        "_target_": "innofw.core.datamodules.lightning_datamodules.detection_coco.CocoLightningDataModule",
        "train": {
            "source": str(get_test_folder_path() / "data/images/detection/wheat")
        },
        "test": {"source": str(get_test_folder_path() / "data/images/detection/wheat")},
        "num_workers": 8,
    }
)

dicom_datamodule_cfg_w_target = DictConfig(
    {
        "task": ["image-detection"],
        "name": "stroke",
        "description": "object detection dataset of wheat",
        "markup_info": "Информация о разметке",
        "date_time": "01.07.2076",
        "_target_": "innofw.core.datamodules.lightning_datamodules.detection_coco.DicomCocoLightningDataModule",
        "train": {
            "source": str(get_test_folder_path() / "data/images/detection/stroke/test/")
        },
        "test": {
            "source": str(get_test_folder_path() / "data/images/detection/stroke/test/")
        },
        "num_workers": 1,
    }
)

arable_segmentation_cfg_w_target = DictConfig(
    {
        "task": ["image-segmentation"],
        "name": "arable",
        "description": "something",
        "markup_info": "something",
        "date_time": "04.08.2022",
        "_target_": "innofw.core.datamodules.lightning_datamodules.segmentation_hdf5_dm.HDF5LightningDataModule",
        "train": {
            "source": str(
                get_test_folder_path() / "data/images/segmentation/arable/train"
            )
        },
        "test": {
            "source": str(
                get_test_folder_path() / "data/images/segmentation/arable/test"
            )
        },
        "channels_num": 4,
    }
)

faces_datamodule_cfg_w_target = DictConfig(
    {
        "task": ["image-classification"],
        "name": "face-recognition",
        "description": "face-recognition",
        "markup_info": "Информация о разметке",
        "date_time": "01.07.2076",
        "_target_": "innofw.core.datamodules.lightning_datamodules.image_folder_dm.ImageLightningDataModule",
        "train": {
            "source": str(
                get_test_folder_path()
                / "data/images/classification/office-character-classification"
            )
        },
        "test": {
            "source": str(
                get_test_folder_path()
                / "data/images/classification/office-character-classification"
            )
        },
        "num_workers": 8,
        "val_size": 0.2,
        "batch_size": 2,
    }
)

qm9_datamodule_cfg_w_target = DictConfig(
    {
        "task": ["qsar-regression"],
        "name": "qm9",
        "description": "https://paperswithcode.com/dataset/qm9",
        "markup_info": "Информация о разметке",
        "date_time": "18.06.2019",
        "_target_": "innofw.core.datamodules.pandas_datamodules.QsarDataModule",
        "train": {
            "source": str(
                get_test_folder_path() / "data/tabular/molecular/smiles/qm9/train"
            )
        },
        "test": {
            "source": str(
                get_test_folder_path() / "data/tabular/molecular/smiles/qm9/train"
            )
        },
        "smiles_col": "smiles",
        "target_col": "gap",
    }
)


tiff_datamodule_cfg_w_target = DictConfig(
    {
        "_target_": "innofw.core.datamodules.lightning_datamodules.semantic_segmentation.tiff_dm.SegmentationDM",
        "train": {
            "source": str(
                get_test_folder_path()
                / "data/images/segmentation/linear-roads-bin-seg-oftp/datamodule_data/train/"
            ),
        },
        "test": {
            "source": str(
                get_test_folder_path()
                / "data/images/segmentation/linear-roads-bin-seg-oftp/datamodule_data/train"
            ),
        },
        "weights_csv_path": None,
        "num_workers": 2,
        "batch_size": 1,
        "channels": 3,
        "name": "something",
        "task": "image-segmentation",
        "description": "some",
        "markup_info": "some",
        "date_time": "some",
    }
)

drugprot_datamodule_cfg_w_target = DictConfig(
    {
        "task": ["text-ner"],
        "name": "Drugprot",
        "description": "something",
        "markup_info": "Информация о разметке",
        "date_time": "18.06.2019",
        "_target_": "innofw.core.datamodules.lightning_datamodules.drugprot.DrugprotDataModule",
        "train": {
            "source": "https://api.blackhole.ai.innopolis.university/public-datasets/drugprot/train.zip",
            "target": "./data/drugprot/train/",
        },
        "test": {
            "source": "https://api.blackhole.ai.innopolis.university/public-datasets/drugprot/test.zip",
            "target": "./data/drugprot/test/",
        },
        "infer": {
            "source": "https://api.blackhole.ai.innopolis.university/public-datasets/drugprot/test.zip",
            "target": "./data/drugprot/infer/",
        },
        "val_size": 0.2,
        "label_dict": {"NA": 0, "PRESENT": 1},
        "tokenizer": {
            "_target_": "transformers.BertTokenizerFast.from_pretrained",
            "pretrained_model_name_or_path": "dmis-lab/biobert-base-cased-v1.2",
        },
        "entity_labelmapper": {
            "_target_": "innofw.core.datamodules.lightning_datamodules.drugprot.LabelMapper",
            "label_dict": {"NA": 0, "PRESENT": 1},
        },
    }
)


faces_siamese_datamodule_cfg_w_target = DictConfig(
    {
        "task": ["one-shot-learning"],
        "name": "osl_faces",
        "description": "something",
        "markup_info": "Информация о разметке",
        "date_time": "18.06.2019",
        "_target_": "innofw.core.datamodules.lightning_datamodules.siamese_dm.SiameseDataModule",
        "train": {
            "source": "https://api.blackhole.ai.innopolis.university/public-datasets/testing/faces/train.zip",
            "target": "./data/osl/train",
        },
        "test": {
            "source": "https://api.blackhole.ai.innopolis.university/public-datasets/testing/faces/test.zip",
            "target": "./data/osl/test/",
        },
        "infer": {
            "source": "https://api.blackhole.ai.innopolis.university/public-datasets/faces/infer.zip",
            "target": "./data/osl/infer",
        },
        "val_size": 0.2,
        "num_workers": 2,
    }
)

qsar_datamodule_cfg_w_target = DictConfig(
    {
        "task": [
            "qsar-regression",
            "text-vae-reverse",
            "text-vae-forward",
            "text-vae",
        ],
        "name": "qm9_selfies",
        "description": "something",
        "markup_info": "Информация о разметке",
        "date_time": "18.06.2019",
        "_target_": "innofw.core.datamodules.lightning_datamodules.QsarSelfiesDataModule",
        "train": {
            "source": "https://api.blackhole.ai.innopolis.university/public-datasets/qm9/train.zip",
            "target": "./data/qm9/train",
        },
        "test": {
            "source": "https://api.blackhole.ai.innopolis.university/public-datasets/qm9/test.zip",
            "target": "./data/qm9/test",
        },
        "infer": {
            "source": "https://api.blackhole.ai.innopolis.university/public-datasets/qm9/test.zip",
            "target": "./data/qm9/infer",
        },
        "smiles_col": "smiles",
        "target_col": "gap",
    }
)
