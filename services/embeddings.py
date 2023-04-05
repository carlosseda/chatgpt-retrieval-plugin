from typing import Dict, List, Optional, Tuple
from models.models import Document, DocumentChunk, DocumentChunkMetadata

import os
import json

def store_embeddings(chunks: List[DocumentChunk]):
  
    if not os.path.exists('./embeddings'):
        os.makedirs('./embeddings')

    for chunk in chunks:
        with open(f'./embeddings/{chunk.metadata.author}_{chunk.metadata.source_id}.jsonl', 'a', encoding='utf-8') as f:
            json.dump({'id': chunk.id, 'text': chunk.text, 'metadata': chunk.metadata.__dict__, 'embedding': chunk.embedding}, f, ensure_ascii=False)
            f.write('\n')