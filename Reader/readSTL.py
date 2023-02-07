import vtk

def main():
    colors = vtk.vtkNamedColors()

    filename = '../data/solid.stl'

    reader = vtk.vtkSTLReader()
    reader.SetFileName(filename)
    print(reader)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    property = vtk.vtkProperty()
    property.SetColor(colors.GetColor3d('white'))
    property.SetDiffuse(0.8)
    property.SetOpacity(0.5)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.SetProperty(property)

    # Create a rendering window and renderer
    ren = vtk.vtkRenderer()

    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetWindowName('ReadSTL')

    # Create a renderwindowinteractor
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Assign actor to the renderer
    ren.AddActor(actor)
    ren.SetBackground(colors.GetColor3d('DarkOliveGreen'))

    # Enable user interface interactor
    iren.Initialize()
    renWin.Render()
    iren.Start()


if __name__ == '__main__':
    main()
