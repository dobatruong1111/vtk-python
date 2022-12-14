# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Read a VTK XML PolyData file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter) # object
    parser.add_argument('filename', help='diskout-stream-binary-zlib.vtp.')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtkNamedColors()

    filename = 'diskout-stream-ascii.vtp' # get_program_parameters()

    reader = vtkXMLPolyDataReader() # reading a .vtp file
    reader.SetFileName(filename)
    reader.Update()

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Tan'))

    # Create a rendering window and renderer
    ren = vtkRenderer()
    # Assign actor to the renderer
    ren.AddActor(actor)
    ren.SetBackground(colors.GetColor3d('AliceBlue'))
    # ren.GetActiveCamera().SetPosition(-0.5, 0.1, 0.0)
    # ren.GetActiveCamera().SetViewUp(0.1, 0.0, 1.0)

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetWindowName('ReadVTP')

    # Create a renderwindowinteractor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    # Enable user interface interactor
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
