import vtk

def main():
    colors = vtk.vtkNamedColors()

    cone = vtk.vtkCubeSource()

    map = vtk.vtkPolyDataMapper()
    map.SetInputConnection(cone.GetOutputPort())

    property = vtk.vtkProperty()
    property.SetColor(colors.GetColor3d("Tomato"))

    actor = vtk.vtkActor()
    actor.SetMapper(map)
    actor.SetProperty(property)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d("CornflowerBlue"))

    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(renderer)
    renWin.SetSize(300, 300)
    renWin.SetWindowName("Cone")

    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Start()

if __name__ == "__main__":
    main()