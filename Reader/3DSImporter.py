import vtkmodules.vtkInteractionStyle
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImport import vtk3DSImporter
from vtkmodules.vtkRenderingCore import (
    vtkCamera,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    filename = '../data/digest_article/Cottage_FREE.3DS'

    importer = vtk3DSImporter()
    importer.SetFileName(filename)
    importer.ComputeNormalsOn()

    ren = vtkRenderer()
    ren.SetBackground2(colors.GetColor3d("white"))
    ren.SetBackground(colors.GetColor3d("black"))
    ren.GradientBackgroundOn()

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetWindowName('3DSImporter')

    importer.SetRenderWindow(renWin)
    importer.Update()

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    actors = ren.GetActors()
    print('There are',actors.GetNumberOfItems(),'actors')
    
    camera = vtkCamera()
    camera.SetPosition(0,-1,0)
    camera.SetFocalPoint(0,0,0)
    camera.SetViewUp(0,0,1)
    camera.Azimuth(150)
    camera.Elevation(30)
    print(camera)

    ren.SetActiveCamera(camera)
    ren.ResetCamera()
    ren.ResetCameraClippingRange()

    renWin.Render()
    iren.Start()

if __name__ == "__main__":
    main()
