import vtk

def main():

    filename = '../data/SCD2001_MR_101.dcm'

    # Reader
    reader = vtk.vtkDICOMImageReader()
    reader.SetFileName(filename)
    reader.Update()

    # Visualize
    imageViewer = vtk.vtkImageViewer2()
    imageViewer.SetInputConnection(reader.GetOutputPort())
    imageViewer.SetSize(300, 300)
    print(reader.GetOutputPort())

    iren = vtk.vtkRenderWindowInteractor()

    imageViewer.SetupInteractor(iren)
    imageViewer.Render()
    imageViewer.GetRenderer().ResetCamera()

    iren.Start()

if __name__ == '__main__':
    main()
