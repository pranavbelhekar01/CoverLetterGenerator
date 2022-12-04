import cohere
class cover_letter:
  def cv(prompt1):

    co = cohere.Client('iSwUoeTncM6gpGVqXJw5DFs2zdaFZbYSPgcXYCIJ')
    response = co.generate(
      model='342dfdb2-0f9d-4b3a-8608-a132648d82a9-ft',
      prompt= prompt1,
      max_tokens=450,
      temperature=0.49,
      k=2,
      p=0.75,
      frequency_penalty=0.134,
      presence_penalty=0,
      stop_sequences=['Sincerely', '[Your Name]'],
      return_likelihoods='NONE')
    return (response.generations[0].text)