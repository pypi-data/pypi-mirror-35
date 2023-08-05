
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>

namespace py = pybind11;
using namespace pybind11::literals;


PYBIND11_DECLARE_HOLDER_TYPE(T, boost::shared_ptr<T>);
#include "../make_opaque_vectors.hpp"

#include "recognition/distance_map.hpp"
#include "recognition/hough_3d.hpp"
#include "recognition/mask_map.hpp"
#include "recognition/orr_octree.hpp"
#include "recognition/orr_octree_zprojection.hpp"
#include "recognition/point_types.hpp"
#include "recognition/quantized_map.hpp"
#include "recognition/region_xy.hpp"
#include "recognition/dense_quantized_multi_mod_template.hpp"
#include "recognition/dot_modality.hpp"
#include "recognition/dotmod.hpp"
#include "recognition/sparse_quantized_multi_mod_template.hpp"
#include "recognition/quantizable_modality.hpp"
#include "recognition/linemod.hpp"
#include "recognition/model_library.hpp"
#include "recognition/hypothesis.hpp"
#include "recognition/rigid_transform_space.hpp"
#include "recognition/implicit_shape_model.hpp"
#include "recognition/surface_normal_modality.hpp"
#include "recognition/line_rgbd.hpp"


void defineRecognitionClasses(py::module &m) {
    py::module m_recognition = m.def_submodule("recognition", "Submodule recognition");
    defineRecognitionDistanceMapClasses(m_recognition);
    defineRecognitionHough3dClasses(m_recognition);
    defineRecognitionMaskMapClasses(m_recognition);
    defineRecognitionOrrOctreeClasses(m_recognition);
    defineRecognitionOrrOctreeZprojectionClasses(m_recognition);
    defineRecognitionPointTypesClasses(m_recognition);
    defineRecognitionQuantizedMapClasses(m_recognition);
    defineRecognitionRegionXyClasses(m_recognition);
    defineRecognitionDenseQuantizedMultiModTemplateClasses(m_recognition);
    defineRecognitionDotModalityClasses(m_recognition);
    defineRecognitionDotmodClasses(m_recognition);
    defineRecognitionSparseQuantizedMultiModTemplateClasses(m_recognition);
    defineRecognitionQuantizableModalityClasses(m_recognition);
    defineRecognitionLinemodClasses(m_recognition);
    defineRecognitionModelLibraryClasses(m_recognition);
    defineRecognitionHypothesisClasses(m_recognition);
    defineRecognitionRigidTransformSpaceClasses(m_recognition);
    defineRecognitionImplicitShapeModelClasses(m_recognition);
    defineRecognitionSurfaceNormalModalityClasses(m_recognition);
    defineRecognitionLineRgbdClasses(m_recognition);
}