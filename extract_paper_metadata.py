#!/usr/bin/env python3
"""
Paper Metadata Extractor using Claude API

This script extracts structured metadata from scientific paper PDFs
using the Claude API. It analyzes nanoparticle drug delivery studies
and outputs data in a standardized 2-column markdown table format.

Usage:
    python extract_paper_metadata.py <pdf_file_path>

    Or use as a module:
    from extract_paper_metadata import extract_metadata
    result = extract_metadata("path/to/paper.pdf", api_key="your_api_key")
"""

import anthropic
import base64
import sys
import os
from pathlib import Path


# System prompt for paper analysis
SYSTEM_PROMPT = """You are a scientific paper analysis expert specializing in pharmaceutical and nanoparticle research.
All responses must be provided in English.

When a paper PDF is attached, analyze it and extract the following items in a 2-column markdown table format:

Required extraction items:
B: DOI
C: Publication_Year
D: NP_Material_Type (Nanoparticle material type)
E: Surface_Modification_Type
F: Surface_Modification_Ligand
G: Particle_Size_nm
H: Zeta_Potential_mV
I: Shape
J: Absorption_Enhancer
K: Dose_mg_per_kg
L: Dose_Total_mg
M: Absorption_Site
N: Animal_Model
O: Fasting_Fed
P: AUC_Absolute_value
Q: AUC_Unit_Original
R: Cmax_value
S: Cmax_Unit_Original
T: Tmax_hour
U: Elimination_Half_Life_hour
V: Bioavailability_F_Percent
W: Comparison_Group_Description
X: Bioavailability_Fold_Change
Y: Clearance_L_h_kg
Z: Volume_Distribution_L_kg
AA: In_Vitro_Data_Available
AB: In_Vitro_Findings_Summary
AC: Data_Completeness_Flag

Response format rules:
- Create a 2-column markdown table with only item codes and content
- Express values as concisely and quantitatively as possible
- Mark items not specified in the paper as "Not reported" or "Not specified"
- Absolutely NO hallucination (false information) - do not guess data not present in the paper
- Abbreviations are allowed (e.g., Amp=Ampicillin, SI=Small Intestine, LI=Large Intestine)
- Provide only the table without additional explanations or code blocks"""


USER_PROMPT = """Please analyze this attached paper PDF and extract the metadata according to the specified format.

Provide the output as a 2-column markdown table with the following structure:

| Item Code | Content |
|-----------|---------|
| B | [DOI] |
| C | [Year] |
| D | [Nanoparticle material] |
... and so on for all items B through AC.

Remember:
- Extract only information explicitly stated in the paper
- Use "Not reported" for missing information
- Be precise with numerical values and units
- No hallucination - only report what is in the paper"""


def read_pdf_as_base64(pdf_path: str) -> str:
    """
    Read a PDF file and return its base64 encoded content.

    Args:
        pdf_path: Path to the PDF file

    Returns:
        Base64 encoded string of the PDF content

    Raises:
        FileNotFoundError: If the PDF file does not exist
        ValueError: If the file is not a PDF
    """
    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if path.suffix.lower() != '.pdf':
        raise ValueError(f"File must be a PDF, got: {path.suffix}")

    with open(path, 'rb') as f:
        pdf_data = f.read()

    return base64.standard_b64encode(pdf_data).decode('utf-8')


def extract_metadata(pdf_path: str, api_key: str = None) -> str:
    """
    Extract metadata from a scientific paper PDF using Claude API.

    Args:
        pdf_path: Path to the PDF file
        api_key: Claude API key. If None, uses ANTHROPIC_API_KEY environment variable

    Returns:
        Markdown table string with extracted metadata

    Raises:
        ValueError: If API key is not provided
        FileNotFoundError: If PDF file does not exist
    """
    # Get API key
    if api_key is None:
        api_key = os.environ.get('ANTHROPIC_API_KEY')

    if not api_key:
        raise ValueError(
            "API key must be provided either as argument or via "
            "ANTHROPIC_API_KEY environment variable"
        )

    # Read and encode PDF
    pdf_base64 = read_pdf_as_base64(pdf_path)

    # Initialize Anthropic client
    client = anthropic.Anthropic(api_key=api_key)

    # Create message with PDF attachment
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": pdf_base64,
                        },
                    },
                    {
                        "type": "text",
                        "text": USER_PROMPT
                    }
                ],
            }
        ],
    )

    # Extract and return the response text
    return message.content[0].text


def main():
    """Main function for command-line usage."""
    if len(sys.argv) < 2:
        print("Usage: python extract_paper_metadata.py <pdf_file_path> [api_key]")
        print("\nEnvironment variables:")
        print("  ANTHROPIC_API_KEY - Claude API key (can be used instead of argument)")
        print("\nExample:")
        print("  python extract_paper_metadata.py paper.pdf")
        print("  python extract_paper_metadata.py paper.pdf your_claude_api_key")
        print("  ANTHROPIC_API_KEY=your_key python extract_paper_metadata.py paper.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]
    api_key = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        result = extract_metadata(pdf_path, api_key)
        print(result)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except anthropic.APIError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
