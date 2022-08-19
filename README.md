# vtk-python
- vtk (visualization toolkit) 
- Object-oriented design
- High level of abstraction (compared to graphics APIs like OpenGL or Direct3D)
## Setup
- Setup Python [download](https://www.python.org/downloads/)
- Command line 
```
pip install vtk
```
## The visualization pipeline
- To visualize your data in VTK
- Set up a pipeline like this:
### Basic 
![pelineBasic](https://user-images.githubusercontent.com/74960507/183383051-6f9a17b5-fa65-421e-9164-1005ff080e4b.PNG)
### Advanced
![pipelineAd](https://user-images.githubusercontent.com/74960507/183382930-47b93ae4-b018-4e14-9434-dacda78599c4.PNG)
### Description
#### Source
- It provides data input
- VTK provides various source classes that can be used to construct simple geometric objects like cones, spheres, cubes,...
- vtkConeSource()
    - Generate polygonal cone
    - It creates a cone centered at a specified point and pointing in a specified direction.
    - By defauld, the center is the origin and the direction is the x axis
#### Reader
- Reads data from file
#### Filter
- Takes data as input, modifies it in some way, and return the modified data
#### Mapper
- Maps data to graphics primitives (points, lines or triangles)
![graphicsprimitives](https://user-images.githubusercontent.com/74960507/183333460-796a8cf6-f2ee-4a82-b0b0-fbcc55406037.PNG)
- That can be displayed by the renderer
- vtkPolyDataMapper()
    - It is a class that maps polygonal data to graphics primitives
#### Actor
- vtkActor()
    - It represents an object (geometry and properties)
#### Renderrer
- Renderer is an object that controls the rendering process for object
- Rendering is the process of converting geometry
#### Render Window
- The vtkRenderWindow() class creates a window for renderers to draw into
#### Interactor
- The vtkRenderWindowInteractor() class provides platform-independent window interaction via the mouse and keyboard
- Allows you to rotate/zoom the camera
## IO - Use Reader
### Reading a .stl file
- [source](https://whatext.com/vi/stl)
- vtkSTLReader is a source object that reads ASCII or binary stereo lithography files (.stl files)
### Reading a .dcm file
- DICOM (stands for digital imaging in communications and medicine) is a medical image file format widely used to exchange data, provided by various modalities
### Reading a .vtp file
- [source](https://whatext.com/vi/vtp)
- vtkXMLPolyDataReader reads the VTK XML PolyData file format
- One PolyData file can be read to produce one output
### Reading a .3ds file
- [source](https://whatext.com/vi/3ds)
- vtk3DSImporter imports 3D studio files into vtk 
