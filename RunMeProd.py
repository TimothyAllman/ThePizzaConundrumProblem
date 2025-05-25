from thepizzaconundrumproblem.EnvFileDataModule import EnvFileData
from thepizzaconundrumproblem.PipelineFunctionsModule import CreatePipeline


myEnvDictionary = EnvFileData(
    myDate="2025-05-16",
    myPrefix="test",
    mySuffix="pizza",
)

dag = CreatePipeline(
    envParams=myEnvDictionary,
)

dag.build(
    force=True,
)
