DIFFICULTY_RATING_PROMPT = r"""
        # CONTEXT #
        I am a teacher, and I have some high-level olympiad math problems. 
        I want to evaluate the difficulty of these math problems. There are some references available regarding the difficulty of the problems:
        <difficulty reference>
        For reference, here are some sample problems from each of the difficulty levels 1-10:

        1: Jamie counted the number of edges of a cube, Jimmy counted the numbers of corners, and Judy counted the number of faces. They then added the three numbers. What was the resulting sum? (2003 AMC 8, Problem 1)

        1: How many integer values of $x$ satisfy $|x| < 3\pi$? (2021 Spring AMC 10B, Problem 1)

        1.5: A number is called flippy if its digits alternate between two distinct digits. For example, $2020$ and $37373$ are flippy, but $3883$ and $123123$ are not. How many five-digit flippy numbers are divisible by $15?$ (2020 AMC 8, Problem 19)

        2: A fair $6$-sided die is repeatedly rolled until an odd number appears. What is the probability that every even number appears at least once before the first occurrence of an odd number? (2021 Spring AMC 10B, Problem 18)

        2.5: $A$, $B$, $C$ are three piles of rocks. The mean weight of the rocks in $A$ is $40$ pounds, the mean weight of the rocks in $B$ is $50$ pounds, the mean weight of the rocks in the combined piles $A$ and $B$ is $43$ pounds, and the mean weight of the rocks in the combined piles $A$ and $C$ is $44$ pounds. What is the greatest possible integer value for the mean in pounds of the rocks in the combined piles $B$ and $C$? (2013 AMC 12A, Problem 16)

        3: Triangle $ABC$ with $AB=50$ and $AC=10$ has area $120$. Let $D$ be the midpoint of $\overline{AB}$, and let $E$ be the midpoint of $\overline{AC}$. The angle bisector of $\angle BAC$ intersects $\overline{DE}$ and $\overline{BC}$ at $F$ and $G$, respectively. What is the area of quadrilateral $FDBG$? (2018 AMC 10A, Problem 24)

        3.5: Find the number of integer values of $k$ in the closed interval $[-500,500]$ for which the equation $\log(kx)=2\log(x+2)$ has exactly one real solution. (2017 AIME II, Problem 7)

        4: Define a sequence recursively by $x_0=5$ and
        \[x_{n+1}=\frac{x_n^2+5x_n+4}{x_n+6}\]
        for all nonnegative integers $n.$ Let $m$ be the least positive integer such that
        \[x_m\leq 4+\frac{1}{2^{20}}.\]
        In which of the following intervals does $m$ lie?

        $\textbf{(A) } [9,26] \qquad\textbf{(B) } [27,80] \qquad\textbf{(C) } [81,242]\qquad\textbf{(D) } [243,728] \qquad\textbf{(E) } [729,\infty)$  
        (2019 AMC 10B, Problem 24 and 2019 AMC 12B, Problem 22)

        4.5: Find, with proof, all positive integers $n$ for which $2^n + 12^n + 2011^n$ is a perfect square. (USAJMO 2011/1)

        5: Find all triples $(a, b, c)$ of real numbers such that the following system holds:
        \[
        a+b+c=\frac{1}{a}+\frac{1}{b}+\frac{1}{c},
        \]
        \[
        a^2+b^2+c^2=\frac{1}{a^2}+\frac{1}{b^2}+\frac{1}{c^2}.
        \]
        (JBMO 2020/1)

        5.5: Triangle $ABC$ has $\angle BAC = 60^{\circ}$, $\angle CBA \leq 90^{\circ}$, $BC=1$, and $AC \geq AB$. Let $H$, $I$, and $O$ be the orthocenter, incenter, and circumcenter of $\triangle ABC$, respectively. Assume that the area of pentagon $BCOIH$ is the maximum possible. What is $\angle CBA$? (2011 AMC 12A, Problem 25)

        6: Let $\triangle ABC$ be an acute triangle with circumcircle $\omega,$ and let $H$ be the intersection of the altitudes of $\triangle ABC.$ Suppose the tangent to the circumcircle of $\triangle HBC$ at $H$ intersects $\omega$ at points $X$ and $Y$ with $HA=3,\ HX=2,$ and $HY=6.$ The area of $\triangle ABC$ can be written in the form $m\sqrt{n},$ where $m$ and $n$ are positive integers, and $n$ is not divisible by the square of any prime. Find $m+n.$ (2020 AIME I, Problem 15)

        6.5: Rectangles $BCC_1B_2,$ $CAA_1C_2,$ and $ABB_1A_2$ are erected outside an acute triangle $ABC.$ Suppose that
        \[\angle BC_1C+\angle CA_1A+\angle AB_1B=180^{\circ}.\]
        Prove that lines $B_1C_2,$ $C_1A_2,$ and $A_1B_2$ are concurrent. (USAMO 2021/1, USAJMO 2021/2)

        7: We say that a finite set $\mathcal{S}$ in the plane is balanced if, for any two different points $A$, $B$ in $\mathcal{S}$, there is a point $C$ in $\mathcal{S}$ such that $AC=BC$. We say that $\mathcal{S}$ is centre-free if for any three points $A$, $B$, $C$ in $\mathcal{S}$, there is no point $P$ in $\mathcal{S}$ such that $PA=PB=PC$.

        Show that for all integers $n\geq 3$, there exists a balanced set consisting of $n$ points.
        Determine all integers $n\geq 3$ for which there exists a balanced centre-free set consisting of $n$ points.
        (IMO 2015/1)

        7.5: Let $\mathbb{Z}$ be the set of integers. Find all functions $f : \mathbb{Z} \rightarrow \mathbb{Z}$ such that
        \[
        xf(2f(y)-x)+y^2f(2x-f(y))=\frac{f(x)^2}{x}+f(yf(y))
        \]
        for all $x, y \in \mathbb{Z}$ with $x \neq 0$. (USAMO 2014/2)

        8: For each positive integer $n$, the Bank of Cape Town issues coins of denomination $\frac1n$. Given a finite collection of such coins (of not necessarily different denominations) with total value at most $99+\frac{1}{2}$, prove that it is possible to split this collection into $100$ or fewer groups, such that each group has total value at most $1$. (IMO 2014/5)

        8.5: Let $I$ be the incentre of acute triangle $ABC$ with $AB\neq AC$. The incircle $\omega$ of $ABC$ is tangent to sides $BC, CA$, and $AB$ at $D, E,$ and $F$, respectively. The line through $D$ perpendicular to $EF$ meets $\omega$ at $R$. Line $AR$ meets $\omega$ again at $P$. The circumcircles of triangle $PCE$ and $PBF$ meet again at $Q$.

        Prove that lines $DI$ and $PQ$ meet on the line through $A$ perpendicular to $AI$. (IMO 2019/6)

        9: Let $k$ be a positive integer and let $S$ be a finite set of odd prime numbers. Prove that there is at most one way (up to rotation and reflection) to place the elements of $S$ around the circle such that the product of any two neighbors is of the form $x^2+x+k$ for some positive integer $x$. (IMO 2022/3)

        9.5: An anti-Pascal triangle is an equilateral triangular array of numbers such that, except for the numbers in the bottom row, each number is the absolute value of the difference of the two numbers immediately below it. For example, the following is an anti-Pascal triangle with four rows which contains every integer from $1$ to $10$.
        \[
        \begin{array}{ c@{\hspace{4pt}}c@{\hspace{4pt}} c@{\hspace{4pt}}c@{\hspace{2pt}}c@{\hspace{2pt}}c@{\hspace{4pt}}c }
        & & & 4 & & & \\
        & & 2 & & 6 & & \\
        & 5 & & 7 & & 1 & \\
        8 & & 3 & & 10 & & 9 \\
        \end{array}
        \]
        Does there exist an anti-Pascal triangle with $2018$ rows which contains every integer from $1$ to $1 + 2 + 3 + \dots + 2018$? (IMO 2018/3)

        10: Prove that there exists a positive constant $c$ such that the following statement is true: Consider an integer $n > 1$, and a set $\mathcal S$ of $n$ points in the plane such that the distance between any two different points in $\mathcal S$ is at least 1. It follows that there is a line $\ell$ separating $\mathcal S$ such that the distance from any point of $\mathcal S$ to $\ell$ is at least $cn^{-1/3}$.

        (A line $\ell$ separates a set of points S if some segment joining two points in $\mathcal S$ crosses $\ell$.) (IMO 2020/6)
        
        ## Arithmetic and Number Operations: Elementary to Advanced Difficulty Guidelines ##
        This subcategory includes problems that involve arithmetic operations from basic to complex, as outlined below:
        
        1 – 2:
          • Basic arithmetic computations (single-digit operations, simple fractions).
          • Suitable for early elementary to middle school.
        
        2.5 – 3:
          • Multi-step computations combining basic operations.
          • Appropriate for middle school students with increased problem-solving skills.
        
        3.5 – 4:
          • Intermediate operations including fractions, decimals, and percentages, requiring logical reasoning.
          • Suitable for advanced middle school or early high school.
        
        4.5 – 6:
          • Multi-layered arithmetic reasoning that may include introductory algebraic manipulation and estimation.
          • Appropriate for high school students with a strong foundation in arithmetic.
        
        6.5 – 8:
          • Challenging problems with non-standard problem structures and deeper insights into number properties.
          • Often used in advanced competitions and high-level problem-solving sessions.
        
        8.5 – 10:
          • Highly challenging problems, where elementary operations are used within intricate and sophisticated arguments.
          • Targeted for elite competitions and advanced mathematical problem-solving.
        
        # OBJECTIVE #
        A. Summarize the math problem in a brief sentence, describing the concepts involved in the math problem.
        B. Based on the source of the given problem, as well as the difficulty of the problems referenced in these materials and the solution to the current problem, please provide 
        an overall difficulty score for the current problem. The score should be a number between 1 and 10, with increments of 0.5, and should align perfectly with the materials.
        
        # STYLE #
        Data report.
        
        # TONE #
        Professional, scientific.
        
        # AUDIENCE #
        Students. Enable them to better understand the difficulty of the math problems.
        
        # RESPONSE: MARKDOWN REPORT #
        ## Summarization
        [Summarize the math problem in a brief paragraph.]
        
        ## Difficulty
        [Rate the difficulty of the math problem and give the reason.]
        
        # ATTENTION #
        - Add "=== report over ===" at the end of the report.
        
        <example math problem>
        The problem requires finding the missing value in the equation

        \[
        \frac{1}{9}+\frac{1}{18}=\frac{1}{\square}.
        \]

        In other words, determine the number that should replace the square such that the sum of the fractions on the left equals the fraction on the right.
        </example math problem>
        
        ## Summarization
        The problem requires finding a value that makes the equation $\\frac{1}{9}+\\frac{1}{18}=\\frac{1}{\\square}$. 
        This involves adding two fractions and determining the equivalent fraction.
        
        ## Difficulty
        Rating: 1
        Reason: This problem is straightforward and primarily involves basic fraction addition, making it suitable for early middle school students. 
        === report over ===
        
        <math problem>
        Let $\mathcal{P}$ be a convex polygon with $n$ sides, $n\ge3$. Any set of $n - 3$ diagonals of $\mathcal{P}$ that do not intersect in the interior of the polygon determine a triangulation of $\mathcal{P}$ into $n - 2$ triangles. If $\mathcal{P}$ is regular and there is a triangulation of $\mathcal{P}$ consisting of only isosceles triangles, find all the possible values of $n$. 
        </math problem>
        
        ## Summarization
        The problem asks for the possible values of $n$ for a regular n-sided polygon that can be completely triangulated into isosceles triangles using non-intersecting diagonals. 
        The solution involves analyzing the properties of the diagonals forming isosceles triangles and deducing that $n$ can be expressed in terms of powers of 2.
        
        ## Difficulty
        Rating: 7
        Reason: The problem involves understanding properties of isosceles triangles in the context of polygon triangulation and requires critical reasoning to establish 
        relationships between the number of sides and powers of 2, making it more complex than typical undergraduate-level problems.
        === report over ===
"""

import json
import sys
import time
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Add path to your API module if necessary
# sys.path.append("your_api_module_path")
from test_api import openai_chat  # Ensure this is correctly imported

def load_system_prompt(prompt_file_path: str) -> str:
    """
    Load the system prompt from a Python file containing a multi-line raw string.
    """
    with open(prompt_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        start_index = content.find('prompt = r"""') + len('prompt = r"""')
        end_index = content.rfind('"""')
        return content[start_index:end_index]


def build_user_prompt(question: str) -> str:
    """
    Build the user prompt for difficulty rating.
    """
    return f'<math problem>\n[Question]: \n{question}\n</math problem>'


def rate_difficulty(record: dict, system_prompt: str) -> dict:
    """
    Rate the difficulty of a single record's question using an LLM.
    """
    question = record.get('question', '')
    user_prompt = build_user_prompt(question)

    try:
        response = openai_chat(system_prompt, user_prompt, model="gpt-4o")

        # Parse the response format
        summarization_start = response.find('## Summarization') + len('## Summarization')
        summarization_end = response.find('## Difficulty')
        summarization = response[summarization_start:summarization_end].strip()

        difficulty_start = response.find('Rating:') + len('Rating:')
        difficulty_end = response.find('Reason:')
        difficulty_rating = response[difficulty_start:difficulty_end].strip()

        reason_start = response.find('Reason:') + len('Reason:')
        reason_end = response.find('=== report over ===')
        difficulty_reason = response[reason_start:reason_end].strip()

        record['difficulty_summarization'] = summarization
        record['difficulty_rating'] = difficulty_rating
        record['difficulty_reason'] = difficulty_reason

    except Exception as e:
        print(f"Error rating difficulty for question: {question}\nException: {e}")
        record['difficulty_summarization'] = 'Unknown'
        record['difficulty_rating'] = 'Unknown'
        record['difficulty_reason'] = 'Unknown'

    return record


def process_file(input_path: str, output_path: str, prompt_path: str, max_workers: int = 20):
    """
    Process the input file and rate question difficulty for each record.
    """
    try:
        system_prompt = load_system_prompt(prompt_path)

        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(rate_difficulty, record, system_prompt) for record in data]
            for future in tqdm(as_completed(futures), total=len(futures), desc="Rating Difficulty"):
                results.append(future.result())
                time.sleep(0.1)  # Optional throttle to avoid API overload

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        print(f"Difficulty classification completed. Output saved to: {output_path}")

    except Exception as e:
        print(f"Error during processing: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rate difficulty of math questions using LLM.")
    parser.add_argument('--input', required=True, help='Path to input JSON file containing questions.')
    parser.add_argument('--output', required=True, help='Path to save the output JSON file with difficulty ratings.')
    parser.add_argument('--prompt', required=True, help='Path to Python file containing the system prompt.')
    parser.add_argument('--workers', type=int, default=20, help='Number of concurrent threads (default: 20).')

    args = parser.parse_args()
    process_file(args.input, args.output, args.prompt, max_workers=args.workers)
