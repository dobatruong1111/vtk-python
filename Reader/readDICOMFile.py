import vtkmodules.vtkInteractionStyle

import vtkmodules.vtkRenderingOpenGL2

import vtk

from vtkmodules.vtkCommonColor import vtkNamedColors

# from vtkmodules.vtkIOImage import vtkDICOMImageReader

from vtkmodules.vtkFiltersSources import (
    vtkConeSource
)

from vtkmodules.vtkRenderingCore import (
    vtkPolyDataMapper,
    vtkActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkProperty
)

def main():
    colors = vtkNamedColors()

    filename = 'SCD2001_MR_101.dcm'

    # Reader
    reader = vtk.vtkDICOMImageReader()
    reader.SetFileName(filename)
    reader.Update()

    # Visualize
    imageViewer = vtk.vtkImageViewer2()
    imageViewer.SetInputConnection(reader.GetOutputPort())
    imageViewer.SetSize(500,500)
    print(reader.GetOutputPort())

    iren = vtkRenderWindowInteractor()

    imageViewer.SetupInteractor(iren)
    imageViewer.Render()
    imageViewer.GetRenderer().ResetCamera()

    iren.Start()

if __name__ == '__main__':
    main()
