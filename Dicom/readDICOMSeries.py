import vtk

def main():
    folder = "../data/digest_article"
    
    imageData = vtk.vtkImageData()
    reader = vtk.vtkDICOMImageReader()
    renderWindow = vtk.vtkRenderWindow()
    renderer = vtk.vtkRenderer()
    interactorStyle = vtk.vtkInteractorStyleTrackballCamera()
    renWinIn = vtk.vtkRenderWindowInteractor()
    volumeMapper = vtk.vtkSmartVolumeMapper()
    volumeProperty = vtk.vtkVolumeProperty()
    gradientOpacity = vtk.vtkPiecewiseFunction()
    scalarOpacity = vtk.vtkPiecewiseFunction()
    color = vtk.vtkColorTransferFunction()
    volume = vtk.vtkVolume()

    reader.SetDirectoryName(folder)
    reader.Update()

    imageData.ShallowCopy(reader.GetOutput())

    renderer.SetBackground(0.1, 0.2, 0.3)

    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(300, 300)

    renWinIn.SetInteractorStyle(interactorStyle)
    renWinIn.SetRenderWindow(renderWindow)

    volumeMapper.SetBlendModeToComposite()
    volumeMapper.SetRequestedRenderModeToGPU()
    volumeMapper.SetInputData(imageData)

    volumeProperty.ShadeOn()
    volumeProperty.SetInterpolationTypeToLinear()

    volumeProperty.SetAmbient(0.1)
    volumeProperty.SetDiffuse(0.9)
    volumeProperty.SetSpecular(0.2)
    volumeProperty.SetSpecularPower(10.0)

    gradientOpacity.AddPoint(0.0, 0.0)
    gradientOpacity.AddPoint(2000.0, 1.0)
    volumeProperty.SetGradientOpacity(gradientOpacity)

    scalarOpacity.AddPoint(-800.0, 0.0)
    scalarOpacity.AddPoint(-750.0, 1.0)
    scalarOpacity.AddPoint(-350.0, 1.0)
    scalarOpacity.AddPoint(-300.0, 0.0)
    scalarOpacity.AddPoint(-200.0, 0.0)
    scalarOpacity.AddPoint(-100.0, 1.0)
    scalarOpacity.AddPoint(1000.0, 0.0)
    scalarOpacity.AddPoint(2750.0, 0.0)
    scalarOpacity.AddPoint(2976.0, 1.0)
    scalarOpacity.AddPoint(3000.0, 0.0)
    volumeProperty.SetScalarOpacity(scalarOpacity)

    color.AddRGBPoint(-750.0, 0.08, 0.05, 0.03)
    color.AddRGBPoint(-350.0, 0.39, 0.25, 0.16)
    color.AddRGBPoint(-200.0, 0.80, 0.80, 0.80)
    color.AddRGBPoint(2750.0, 0.70, 0.70, 0.70)
    color.AddRGBPoint(3000.0, 0.35, 0.35, 0.35)
    volumeProperty.SetColor(color)

    volume.SetMapper(volumeMapper)
    volume.SetProperty(volumeProperty)
    renderer.AddVolume(volume)
    renderer.ResetCamera()

    renderWindow.Render()
    renWinIn.Start()

if __name__ == "__main__":
    main()
