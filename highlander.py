#replace the real polymer by dart-polymer (there can only be one)

import os

bowerLocation = 'web/bower_components/' #location of the bower_components folder
dartElementsLocation = 'packages/polymer_elements/' #location of the polymer_elements dart-dependency

#locations of different polymer-versions inside bower_components
polymerLocations = ['polymer/polymer.html',
'polymer/polymer-micro.html',
'polymer/polymer-mini.html'
]

#proxy polymer to the dart-version
polymerProxy = '<link rel="import" href="../../../packages/web_components/interop_support.html"><link rel="import" href="../../../packages/polymer_interop/polymer.html"><script></script>';

#replace polymers by the dart-version
for polymer in polymerLocations:
    os.remove(bowerLocation + polymer)
    with open(bowerLocation + polymer, "w") as text_file:
        text_file.write(polymerProxy)

#proxy references to base-elements (polymer-elements) to the dart version
installedBowerComponents = filter(os.path.isdir,
                  [os.path.join(bowerLocation, f) for f in os.listdir(bowerLocation)])

for componentPath in installedBowerComponents:
    component = os.path.basename(os.path.normpath(componentPath))
    dartFilename = component.replace("-","_") + ".html"
    #check whether a dart-version of a bower_component exists
    if os.path.isfile(dartElementsLocation + dartFilename):
        #replace by dart-proxy
        proxy = '<link rel="import" href="../../../packages/polymer_elements/{filename}">'.format(filename=dartFilename)
        bowerFilename = bowerLocation + component + "/" + component + ".html" #entrypoint of bower-component is componentname.html
        print "replace " + bowerFilename + " by proxy"
        os.remove(bowerFilename)
        with open(bowerFilename, "w") as text_file:
            text_file.write(proxy)