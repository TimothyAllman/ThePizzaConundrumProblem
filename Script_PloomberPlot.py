from ploomberpipelinetemplate.EnvFileDataModule import EnvFileData
from ploomberpipelinetemplate.PipelineFunctionsModule import CreatePipeline


myEnvDictionary = EnvFileData(
    myPrefix="this_thing",
    mySuffix="prod",
)

dag = CreatePipeline(
    envParams=myEnvDictionary,
)

dag.plot(
    output="myPipeline/DiagramOfProcessFlow.html",
    backend="mermaid",
)
