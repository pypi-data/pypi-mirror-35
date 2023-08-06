import ctypes
import enum
import os.path
import uuid

import laspy
import plyfile
import numpy

import cepton_sdk.point

__all__ = [
    "load_points",
    "PointsFileType",
    "save_points",
]


def save_points_las(points, path):
    """Save points to LAS file.
    """
    header = laspy.header.Header()
    header.data_format_id = 1

    with laspy.file.File(path, mode="w", header=header) as f:
        f.header.gps_time_type = 1
        f.header.guid = uuid.uuid1()
        f.header.scale = [0.001] * 3

        f.gps_time = numpy.remainder(points.timestamps, 1e9)
        f.x = points.positions[:, 0]
        f.y = points.positions[:, 1]
        f.z = points.positions[:, 2]
        f.intensity = points.intensities


def load_points_las(load_path, cls=cepton_sdk.point.Points):
    """Load points from LAS file.

    Returns:
        Points
    """
    data = {}
    with laspy.file.File(load_path, mode="r") as f:
        points = cls(len(f.x))
        points.timestamps[:] = f.gps_time
        points.positions[:, 0] = f.x
        points.positions[:, 1] = f.y
        points.positions[:, 2] = f.z
        points.intensities[:] = f.intensity
    return points, data


class PlyPoint(ctypes.Structure):
    _fields_ = [
        ("position", 3 * ctypes.c_float),
    ]


def save_points_ply(points, path):
    """Save points to PLY file.
    """
    n = len(points)

    with open(path, "w") as f:
        lines = [
            "ply\n",
            "format binary_little_endian 1.0\n",
            "element vertex {}\n".format(len(points)),
            "property float x\n",
            "property float y\n",
            "property float z\n",
            "end_header\n",
        ]
        f.writelines(lines)

    dtype = numpy.dtype(PlyPoint)
    data = numpy.zeros([n], dtype=dtype)
    data["position"][:, :] = points.positions
    with open(path, "ab") as f:
        f.write(data.tobytes())


def load_points_ply(path):
    """Load points from PLY file.

    Returns:
        Points
    """
    plydata = plyfile.PlyData.read(input_path)
    data = plydata.elements[0].data
    n = len(data)
    points = cepton_sdk.Points(n)
    points.positions[:, 0] = data["x"]
    points.positions[:, 1] = data["y"]
    points.positions[:, 2] = data["z"]
    return points


class PcdPoint(ctypes.Structure):
    _fields_ = [
        ("position", 3 * ctypes.c_float),
    ]


def save_points_pcd(points, path):
    """Save points to PCD file.
    """
    n = len(points)

    with open(path, "w") as f:
        lines = [
            "VERSION 0.7\n",
            "FIELDS x y z\n",
            "SIZE 4 4 4\n",
            "TYPE F F F\n",
            "COUNT 1 1 1\n",
            "WIDTH {}\n".format(n),
            "HEIGHT 1\n",
            "VIEWPOINT 0 0 0 1 0 0 0\n",
            "POINTS {}\n".format(n),
            "DATA binary\n",
        ]
        f.writelines(lines)

    dtype = numpy.dtype(PcdPoint)
    data = numpy.zeros([n], dtype=dtype)
    data["position"][:, :] = points.positions
    with open(path, "ab") as f:
        f.write(data.tobytes())


def load_points_pcd(points):
    """Load points from PCD file.

    Returns:
        Points
    """
    raise NotImplementedError()


@enum.unique
class PointsFileType(enum.Enum):
    LAS = 1
    PCD = 2
    PLY = 3


def get_points_file_type(ext):
    return PointsFileType[ext.upper()]


def get_points_file_type_extension(file_type):
    return ".{}".format(file_type.name.lower())


def save_points(points, path, file_type=PointsFileType.LAS):
    """Save points to file.

    Sets file extension based on type.
    """
    ext = get_points_file_type_extension(file_type)
    path = os.path.splitext(path)[0] + ext
    if file_type == PointsFileType.LAS:
        save_points_las(points, path)
    elif file_type == PointsFileType.PCD:
        save_points_pcd(points, path)
    elif file_type == PointsFileType.PLY:
        save_points_ply(points, path)
    else:
        raise NotImplementedError()


def load_points(path, file_type=None):
    """Load points from file.

    File type is inferred from extension.
    """
    if file_type == None:
        ext = os.path.splitext(path)[1]
        file_type = get_points_file_type(ext)
    if file_type == PointsFileType.LAS:
        return load_points_las(path)
    elif file_type == PointsFileType.PCD:
        return load_points_pcd(path)
    elif file_type == PointsFileType.PLY:
        return load_points_ply(path)
    else:
        raise NotImplementedError()
