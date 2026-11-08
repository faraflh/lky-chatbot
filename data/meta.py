# Source register: existing books + additional PDFs from the speeches folder.
# Upload/copy all listed PDFs to the corresponding Google Drive folder before extraction.
# Verify metadata marked None or provisional before using the documents.

SOURCES = [
    # =========================================================
    # BOOKS
    # =========================================================
    {
        "id": "lky_from_third_world_to_first_2000",
        "title": "From Third World to First: The Singapore Story, 1965–2000",
        "author": "Lee Kuan Yew",
        "year": 2000,
        "document_type": "book",
        "topic_tags": [
            "Singapore",
            "economic development",
            "nation building",
            "politics",
            "governance",
            "international relations"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/From-Third-World-to-First-World_The-Singapore-Story-1965-2000-Lee-Kwan-Yew.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English"
    },
    {
        "id": "lky_one_mans_view_2013",
        "title": "One Man’s View of the World",
        "author": "Lee Kuan Yew",
        "year": 2013,
        "document_type": "book",
        "topic_tags": [
            "geopolitics",
            "international relations",
            "global economy",
            "China",
            "United States",
            "Asia",
            "world politics"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/one_mans_view.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English"
    },
    {
        "id": "lky_the_singapore_story_1998",
        "title": "The Singapore Story: Memoirs of Lee Kuan Yew",
        "author": "Lee Kuan Yew",
        "year": 1998,
        "document_type": "book",
        "topic_tags": [
            "Singapore history",
            "independence",
            "politics",
            "leadership",
            "nation building",
            "Malaysia",
            "colonial history"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/the-singapore-story-memoirs-of-lee-kuan-yew-981-204-983-5_compress.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English"
    },
    {
        "id": "lky_hard_truths_to_keep_singapore_going",
        "title": "Hard Truths to Keep Singapore Going",
        "author": "Lee Kuan Yew",
        "year": None,
        "document_type": "book",
        "topic_tags": [
            "Singapore",
            "governance",
            "politics",
            "economic development",
            "leadership",
            "society"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/lee-kuan-yew-hard-truths-to-keep-singapore-going.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English"
    },

    # =========================================================
    # SPEECHES - NATIONAL ARCHIVES OF SINGAPORE (NAS)
    # =========================================================
    {
        "id": "nas_lky19660810",
        "title": "NAS archival speech/document (lky19660810) — verify official title",
        "author": "Lee Kuan Yew",
        "year": 1966,
        "document_type": "speech",
        "topic_tags": [
            "Singapore",
            "politics",
            "history",
            "governance"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/lky19660810.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English — verify against original record"
    },
    {
        "id": "nas_lky19660719",
        "title": "NAS archival speech/document (lky19660719) — verify official title",
        "author": "Lee Kuan Yew",
        "year": 1966,
        "document_type": "speech",
        "topic_tags": [
            "Singapore",
            "politics",
            "history",
            "governance"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/lky19660719.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English — verify against original record"
    },
    {
        "id": "nas_lky19651211c",
        "title": "NAS archival speech/document (lky19651211c) — verify official title",
        "author": "Lee Kuan Yew",
        "year": 1965,
        "document_type": "speech",
        "topic_tags": [
            "Singapore",
            "politics",
            "history",
            "governance"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/lky19651211c.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English — verify against original record"
    },
    {
        "id": "nas_lky19651211a",
        "title": "NAS archival speech/document (lky19651211a) — verify official title",
        "author": "Lee Kuan Yew",
        "year": 1965,
        "document_type": "speech",
        "topic_tags": [
            "Singapore",
            "politics",
            "history",
            "governance"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/lky19651211a.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English — verify against original record"
    },
    {
        "id": "nas_lky19651108",
        "title": "NAS archival speech/document (lky19651108) — verify official title",
        "author": "Lee Kuan Yew",
        "year": 1965,
        "document_type": "speech",
        "topic_tags": [
            "Singapore",
            "politics",
            "history",
            "governance"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/lky19651108.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English — verify against original record"
    },
    {
        "id": "nas_lky19650814",
        "title": "NAS archival speech/document (lky19650814) — verify official title",
        "author": "Lee Kuan Yew",
        "year": 1965,
        "document_type": "speech",
        "topic_tags": [
            "Singapore",
            "politics",
            "history",
            "governance"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/lky19650814.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English — verify against original record"
    },
    {
        "id": "nas_lky19650530a",
        "title": "NAS archival speech/document (lky19650530a) — verify official title",
        "author": "Lee Kuan Yew",
        "year": 1965,
        "document_type": "speech",
        "topic_tags": [
            "Singapore",
            "politics",
            "history",
            "governance"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/lky19650530a.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English — verify against original record"
    },
    {
        "id": "nas_lky19650809b",
        "title": "NAS archival speech/document (lky19650809b) — verify official title",
        "author": "Lee Kuan Yew",
        "year": 1965,
        "document_type": "speech",
        "topic_tags": [
            "Singapore",
            "politics",
            "history",
            "governance"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/lky19650809b.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English — verify against original record"
    },

    # =========================================================
    # ARTICLES
    # =========================================================
    {
        "id": "lky_asian_values_debate",
        "title": "Lee Kuan Yew and the Asian Values Debate",
        "author": "Not confirmed from filename",
        "year": None,
        "document_type": "article",
        "topic_tags": [
            "Asian values",
            "political culture",
            "governance",
            "democracy",
            "Singapore"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/Lee Kuan Yew and the Asian values debate.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English"
    },
    {
        "id": "lky_grand_masters_insights_china_us_world",
        "title": "Lee Kuan Yew: The Grand Master's Insights on China, the United States and the World",
        "author": "Not confirmed from filename",
        "year": None,
        "document_type": "interview_or_article",
        "topic_tags": [
            "China",
            "United States",
            "geopolitics",
            "international relations",
            "Asia"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/lee-kuan-yew-the-grand-masters-insights-on-china-the-united-states-and-the-world.pdf",
        "rights_status": "VERIFY FILE AND RIGHTS BEFORE USE",
        "language": "English"
    },

    # =========================================================
    # INTERVIEWS
    # =========================================================
    {
        "id": "zakaria_lky_culture_is_destiny_1994",
        "title": "Culture Is Destiny: A Conversation with Lee Kuan Yew",
        "author": "Fareed Zakaria and Lee Kuan Yew",
        "year": 1994,
        "document_type": "interview",
        "topic_tags": [
            "politics",
            "governance",
            "Asian values",
            "culture",
            "economic development",
            "international relations"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/Zakaria_LeeKuanYew.pdf",
        "source_url": "http://www.jstor.org/stable/20045923",
        "publication": "Foreign Affairs, Vol. 73, No. 2, pp. 109–126",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English"
    },

    # =========================================================
    # BIOGRAPHIES AND COMPILATIONS
    # =========================================================
    {
        "id": "lky_the_man_and_his_ideas",
        "title": "Lee Kuan Yew: The Man and His Ideas",
        "author": "Not confirmed from filename",
        "year": None,
        "document_type": "book_or_compilation",
        "topic_tags": [
            "biography",
            "leadership",
            "Singapore history",
            "politics",
            "governance"
        ],
        "file_path": "/content/drive/MyDrive/LKY_Knowledge_Base/LKY_The_Man_And_His_Ideas.pdf",
        "rights_status": "REVIEW BEFORE REDISTRIBUTION",
        "language": "English"
    }
]

print(f"Registered sources: {len(SOURCES)}")