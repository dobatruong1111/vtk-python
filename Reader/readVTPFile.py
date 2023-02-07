import vtk

def main():
    colors = vtk.vtkNamedColors()

    filename = '../data/diskout-stream-ascii.vtp'

    reader = vtk.vtkXMLPolyDataReader() # reading a .vtp file
    reader.SetFileName(filename)
    reader.Update()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Tan'))

    # Create a rendering window and renderer
    ren = vtk.vtkRenderer()
    # Assign actor to the renderer
    ren.AddActor(actor)
    ren.SetBackground(colors.GetColor3d('AliceBlue'))

    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetWindowName('ReadVTP')

    # Create a renderwindowinteractor
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    # Enable user interface interactor
    iren.Start()

if __name__ == '__main__':
    main()
