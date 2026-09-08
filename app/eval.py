from ragas import evaluate
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.metrics import (
    LLMContextPrecisionWithReference,
    LLMContextRecall,
    Faithfulness,
    ResponseRelevancy,
)
from ragas.run_config import RunConfig

def evaluateWithRagas(evaluation_dataset, evaluator_llm, evaluator_embeddings):
    

    run_config = RunConfig(
        timeout=180,       # give slow/throttled Groq calls more room
        max_retries=15,    # retry through transient rate-limit backoffs
        max_wait=90,       # cap between-retry wait
        max_workers=2,     # the real fix — drastically reduces concurrent calls hitting Groq's rate limit
    )

    result = evaluate(
        dataset=evaluation_dataset,
        metrics=[
            LLMContextPrecisionWithReference(),
            LLMContextRecall(),
            Faithfulness(),
            ResponseRelevancy(strictness=1),
        ],
        llm=evaluator_llm,
        embeddings=evaluator_embeddings,
        run_config=run_config,
    )
 
    return result