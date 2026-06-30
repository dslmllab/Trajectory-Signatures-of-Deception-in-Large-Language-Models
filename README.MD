




```
llm_trajectory_toolkit/
├── capture/               # Hook-based hidden state extraction
├── geometry/              # 7 geometric feature computation
├── prompts/               # Prompt generation + dataset loading
├── models/                # Model adapters + device-specific loaders
├── analysis/              # Statistical tests + ML classification
├── storage_backend.py     # HDF5 persistence
├── system.py              # Hardware detection
├── api.py                 # High-level TrajectoryAnalyzer
```


## Citation

If you use our LLM Trajectory in your research, please cite:

```bibtex
@inproceedings{mothukuri-parizi-2026-trajectory,
    title = "Trajectory Signatures of Deception in Large Language Models",
    author = "Mothukuri, Viraaji  and Parizi, Reza M.",
    editor = "Liakata, Maria  and
      Moreira, Viviane P.  and
      Zhang, Jiajun  and
      Jurgens, David",
    booktitle = "Proceedings of the 64th Annual Meeting of the {A}ssociation for {C}omputational {L}inguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2026",
    address = "San Diego, California, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.acl-long.1582/",
    pages = "34264--34276",
    ISBN = "979-8-89176-390-6"
}

```