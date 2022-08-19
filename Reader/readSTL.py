# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2

from vtkmodules.vtkCommonColor import vtkNamedColors

from vtkmodules.vtkIOGeometry import vtkSTLReader

from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkProperty
)


def get_program_parameters():
    import argparse
    description = 'Read a .stl file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='.stl')
    args = parser.parse_args()
    return args.filename


def main():
    colors = vtkNamedColors()

    filename = '.\stl_image\solid.stl' # get_program_parameters()

    reader = vtkSTLReader()
    reader.SetFileName(filename)
    print(reader)

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    property = vtkProperty()
    property.SetColor(colors.GetColor3d('white'))
    property.SetDiffuse(0.8)
    property.SetOpacity(0.5)

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.SetProperty(property)

    # Create a rendering window and renderer
    ren = vtkRenderer()

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetWindowName('ReadSTL')

    # Create a renderwindowinteractor
    iren = vtkRenderWindowInteractor()
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
