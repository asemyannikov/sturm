#!/usr/bin/env python3
import re

with open('/tmp/original_hildebrand.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# 1. Replace the TOC
# ============================================================
old_toc = '''    <div class="toc">
        <ul>
            <li><a href="#abstract">1. Abstract and Thesis of the Aporia</a></li>
            <li><a href="#foundation">2. Foundation: Value as the Source of Motivation</a>
                <ul>
                    <li><a href="#importance">2.1. Importance and Its Three Categories</a></li>
                    <li><a href="#two-values">2.2. Two Kinds of Values: Object-Value and Moral Value</a></li>
                    <li><a href="#value-response">2.3. Value-Response</a></li>
                </ul>
            </li>
            <li><a href="#strategy">3. From the False Attack to the True One</a>
                <ul>
                    <li><a href="#principles">3.1. The Six Principles</a></li>
                    <li><a href="#false-attack">3.2. Why the Direct Attack via «Impurity of Motive» Fails</a></li>
                </ul>
            </li>
            <li><a href="#aporia">4. The Aporia of the Heart</a>
                <ul>
                    <li><a href="#scope">4.1. Scope</a></li>
                    <li><a href="#tension">4.2. The Key Tension</a></li>
                    <li><a href="#axioms">4.3. Axioms</a></li>
                    <li><a href="#theorem">4.4. Theorem (The Aporia of the Heart)</a></li>
                    <li><a href="#consequence">4.5. Consequence: The Affective Sphere as Debit Without Credit</a></li>
                </ul>
            </li>
            <li><a href="#objections">5. Three Objections</a></li>
            <li><a href="#asymmetry">6. The Decisive Blow: Asymmetry of Sanction and Disavowal</a>
                <ul>
                    <li><a href="#eidetic">6.1. Can the Asymmetry Be Grounded Eidetically?</a></li>
                    <li><a href="#dilemma">6.2. The Final Dilemma</a></li>
                </ul>
            </li>
            <li><a href="#second-edge">7. The Second Edge: The Aporia of Locus (Volitional Responses)</a></li>
            <li><a href="#limits">8. What the Aporia Does Not Prove</a></li>
            <li><a href="#defenses">9. Anticipation of Defenses</a>
                <ul>
                    <li><a href="#defense-1">9.1. Self-Transcendence vs. Self-Objectification</a></li>
                    <li><a href="#defense-2">9.2. Eidetic Status of Asymmetry via Ontology of Good and Evil</a></li>
                    <li><a href="#defense-3">9.3. Contrition as «Kenosis»</a></li>
                </ul>
            </li>
        </ul>
    </div>'''

new_toc = '''    <div class="toc">
        <ul>
            <li><a href="#abstract">1. Abstract, Thesis, and Illustrative Example</a></li>
            <li><a href="#foundation">2. Foundation: Value as the Source of Motivation</a>
                <ul>
                    <li><a href="#importance">2.1. Importance and Its Three Categories</a></li>
                    <li><a href="#two-values">2.2. Two Kinds of Values: Object-Value and Moral Value</a></li>
                    <li><a href="#value-response">2.3. Value-Response</a></li>
                </ul>
            </li>
            <li><a href="#principles">3. The Six Principles</a></li>
            <li><a href="#aporia">4. The Aporia of the Heart</a>
                <ul>
                    <li><a href="#scope">4.1. Scope</a></li>
                    <li><a href="#tension">4.2. The Key Tension</a></li>
                    <li><a href="#axioms">4.3. Axioms</a></li>
                    <li><a href="#theorem">4.4. Theorem (The Aporia of the Heart)</a></li>
                    <li><a href="#consequence">4.5. Consequence: The Affective Sphere as Debit Without Credit</a></li>
                </ul>
            </li>
            <li><a href="#objections">5. Three Objections</a></li>
            <li><a href="#asymmetry">6. The Decisive Blow: Asymmetry of Sanction and Disavowal</a>
                <ul>
                    <li><a href="#eidetic">6.1. Can the Asymmetry Be Grounded Eidetically?</a></li>
                    <li><a href="#dilemma">6.2. The Final Dilemma</a></li>
                </ul>
            </li>
            <li><a href="#limits">7. What the Aporia Does Not Prove</a></li>
            <li><a href="#defenses">8. Anticipation of Defenses</a>
                <ul>
                    <li><a href="#defense-1">8.1. Self-Transcendence vs. Self-Objectification</a></li>
                    <li><a href="#defense-2">8.2. Eidetic Status of Asymmetry via Ontology of Good and Evil</a></li>
                    <li><a href="#defense-3">8.3. Contrition as «Kenosis»</a></li>
                </ul>
            </li>
        </ul>
    </div>'''

content = content.replace(old_toc, new_toc)

# ============================================================
# 2. Replace section 1 heading and add example after thesis
# ============================================================
content = content.replace(
    '<h2 id="abstract">1. Abstract and Thesis of the Aporia</h2>',
    '<h2 id="abstract">1. Abstract, Thesis, and Illustrative Example</h2>'
)

old_thesis_end = '''        The justification of the thesis reduces to the fact that the necessary condition for achieving the full moral value of an affective response (the act of sanction, <em>Principle 2</em>) logically entails the thematization of the moral quality of one's own act (<em>Principle 6</em>). However, such thematization, by virtue of the established prohibition (<em>Principle 5</em>), destroys this very moral value. The affective sphere thus turns into a domain where moral guilt is possible, but moral merit is structurally unattainable.
    </p>

    <!-- ================================================================== -->
    <!-- 2. Foundation -->
    <!-- ================================================================== -->'''

new_thesis_end = '''        The justification of the thesis reduces to the fact that the necessary condition for achieving the full moral value of an affective response (the act of sanction, <em>Principle 2</em>) logically entails the thematization of the moral quality of one's own act (<em>Principle 6</em>). However, such thematization, by virtue of the established prohibition (<em>Principle 5</em>), destroys this very moral value. The affective sphere thus turns into a domain where moral guilt is possible, but moral merit is structurally unattainable.
    </p>

    <h3>Illustrative Example: The Paradox of Contrition</h3>
    <p>
        To make the aporia tangible before the formal proof, consider a paradigmatic case: <em>contrition</em> – deep repentance in the face of one's own moral evil.
    </p>
    <p>
        Von Hildebrand regards contrition as one of the highest affective value-responses. He speaks of «the moral beauty of a deep contrition» (ch.27, p.319) and lists it alongside love and reverence among those responses whose moral dignity his book is written to defend (ch.27, p.326). At the same time, he explicitly prescribes the reflexive contemplation of one's own moral evil as «legitimate and even morally obligatory» (ch.19, p.243): in contrition, one's own sinfulness is the very object of the act.
    </p>
    <p>
        Now, for this contrition to attain full moral value – to become not merely a spontaneous feeling but a morally meritorious act of the heart – it must be <em>sanctioned</em>: the free spiritual centre must say «Yes» to it, identifying itself with the response (ch.25, p.299; ch.27, p.318). But sanction is possible <em>only</em> toward a morally positive response (ch.25, p.302). Consequently, to sanction my contrition, I must grasp it as morally good.
    </p>
    <p>
        Here the trap closes. The moment I grasp the moral goodness of my contrition, I am thematizing the moral value of my own act – precisely what von Hildebrand prohibits as destructive: «We are unable to look at them lest we distort the normal and genuine accomplishment of our attitude» (ch.19, p.242). The look at the moral beauty of my own repentance poisons the repentance itself, turning self-abasement into a subtle form of self-admiration.
    </p>
    <p>
        Yet if I do <em>not</em> look – if I refrain from grasping the moral quality of my contrition – then I cannot sanction it, for I cannot distinguish sanction from its «diabolical caricature» (ch.25, p.305). Without sanction, the contrition remains a spontaneous affective movement, «not sufficiently connected with our freedom to constitute a morally good attitude in the full sense» (ch.25, p.309). It may render me lovable, but it cannot be imputed to me as moral merit.
    </p>
    <blockquote>
        <strong>The paradox:</strong> I am obliged, in one and the same complex act, to (1) thematize my own moral evil – this is prescribed; (2) grasp the moral goodness of this thematizing – this is required by sanction; and (3) <em>not</em> grasp the moral goodness of this thematizing – this is prohibited by the ban on the «squinting look». The heart that repents most deeply is the heart least permitted to know the worth of its own repentance.
    </blockquote>
    <p>
        The formal proof below (§4) demonstrates that this paradox is not peculiar to contrition but affects <em>every</em> affective value-response in Hildebrand's system.
    </p>

    <!-- ================================================================== -->
    <!-- 2. Foundation -->
    <!-- ================================================================== -->'''

content = content.replace(old_thesis_end, new_thesis_end)

# ============================================================
# 3. Replace section 3 heading and intro (remove "False Attack" framing)
# ============================================================
old_section3 = '''    <h2 id="strategy">3. From the False Attack to the True One</h2>
    <p>
        The argument proceeds in four steps. First, six principles that Hildebrand asserts himself are isolated. Then it is shown why the most obvious route of attack – via «contamination of motive» – is already foreseen and blocked by his own text. Then the aporia is presented, striking not at motives but at the <em>intentional structure</em> of the moral act. And finally it is shown that the only ground on which Hildebrand can defend himself is of an ascetic-theological nature, and that the attempt to ground it eidetically does not dissolve the aporia but sharpens it – which constitutes the final dilemma.
    </p>

    <h3 id="principles">3.1. The Six Principles</h3>
    <p>
        To formulate the aporia, it is necessary to fix six principles that von Hildebrand asserts explicitly and which form the load-bearing structure of his system:
    </p>'''

new_section3 = '''    <h2 id="principles">3. The Six Principles</h2>
    <p>
        To formulate the aporia, it is necessary to fix six principles that von Hildebrand asserts explicitly and which form the load-bearing structure of his system:
    </p>'''

content = content.replace(old_section3, new_section3)

# ============================================================
# 4. Remove §3.2 (False Attack) entirely
# ============================================================
old_false_attack = '''    <h3 id="false-attack">3.2. Why the Direct Attack via «Impurity of Motive» Fails</h3>
    <p>
        The obvious move looks like this. Hildebrand demands that the response be motivated by «nothing but the value» (p.218), and at the same time asserts that an adequate response realizes a distinct metaphysical value (p.225). Hence, a subject who knows the latter acquires a second motive – the desire to realize that metaphysical value. This motive is directed not at the object but at the subject himself. Therefore, purity is violated, and the response turns out to be «moral narcissism under the mask of virtue.»
    </p>
    <p>
        This reasoning possesses superficial persuasiveness but is untenable, for three independent reasons. All three rest on chapter 19 («Moral Consciousness»), which is devoted precisely to this objection.
    </p>
    <p>
        <strong>First, Hildebrand does not merely <em>permit</em> a «second motive» – he <em>requires</em> it.</strong>
    </p>
    <blockquote>
        «…in addition to the response to the value on the object side, it implies a general response to moral goodness as such. &lt;…&gt; The moral significance of responding to the value on the object side is present to his mind and plays a decisive role in the motivation of his act. We could say every morally good value response implies in some way the general will to be morally good, to act and behave in a morally right manner.» (ch.19, p.238)
    </blockquote>
    <p>
        The presence of a motive $m_1$ in the structure of the response is not a defect but a direct assertion of the system. An attack that proves the existence of $m_1$ refutes nothing.
    </p>
    <p>
        <strong>Second, this second motive is itself a pure value-response.</strong>
    </p>
    <blockquote>
        «The will to be morally good is itself a pure value response.» (ch.19, p.238)
    </blockquote>
    <blockquote>
        «…the desire to possess moral values is primarily and by its very nature a value response, and only secondarily a response to an objective good for the person. &lt;…&gt; it is always a pure value response.» (ch.29, p.371)
    </blockquote>
    <p>
        <strong>Third, the requirement «nothing but the value» excludes not other <em>values</em> but other <em>categories of importance</em>.</strong>
    </p>
    <blockquote>
        «The moment our attitude is motivated by other kinds of importance (for example, by something subjectively satisfying or dissatisfying which the object may accidentally have for us in addition to, but independently of, its value), then the positive or negative character of the content of our response need no longer agree with the positive or negative character of the importance in itself which the object possesses.» (ch.17, p.218)
    </blockquote>
    <p>
        What is prohibited is the admixture of the <em>merely subjectively satisfying</em> and the <em>objective good for the person</em>, not every motive distinct from the value of the given object. Since $m_1$ is a response to value (to moral goodness as such), it passes the purity criterion.
    </p>
    <p>
        <strong>Conclusion:</strong> the aporia cannot be built on the concept of impurity. It must be built on the concept of <em>reflexivity</em>.
    </p>

    <!-- ================================================================== -->
    <!-- 4. The Aporia of the Heart -->
    <!-- ================================================================== -->'''

new_after_principles = '''
    <!-- ================================================================== -->
    <!-- 4. The Aporia of the Heart -->
    <!-- ================================================================== -->'''

content = content.replace(old_false_attack, new_after_principles)

# ============================================================
# 5. Remove §7 (Second Edge) entirely
# ============================================================
old_second_edge = '''    <h2 id="second-edge">7. The Second Edge: The Aporia of Locus (Volitional Responses)</h2>
    <p>
        The Aporia of the Heart by construction does not touch volitional responses: for them sanction is not required, and Horn 2 does not operate. But there is a separate, weaker edge that reaches them as well. I mark its weakness explicitly: it does not force a contradiction but presents a bill.
    </p>
    <p>
        The third condition of the moral value of any act, including a volitional one, is this: «the value response must be based on an awareness of the moral significance of the situation, and imply a general will to be morally good» (p.318). Thus moral significance enters the consciousness of the subject necessarily and in all cases. Yet the bearer of moral value is the act of the subject itself (p.153), while Hildebrand needs the moral significance to be given «as much on the object side as the good is which calls for that action» (p.242).
    </p>
    <p>
        The only coherent reconstruction of this thesis is a type/token distinction: the subject thematizes the moral goodness of <em>the action as such</em> («the moral goodness of the action or attitude as such, as a task which we want to fulfill», p.242), not the moral value of their particular act. Against this stand two considerations. The metaphysical value, by p.225, is realized «in the fact that an adequate response is given» – i.e. in the token, not the type; and Hildebrand calls the corresponding attitude «the will to be morally good» – a will <em>to be</em> good, i.e. a will whose object is the moral quality of the one who wills, not an impersonal «let good be done».
    </p>
    <p>
        This is insufficient for a contradiction: Hildebrand can reply that the general will to the good is superactual and therefore does not thematize the given token. I do not build a theorem on this. But the bill is presented: the type/token distinction is necessary to the system and is not carried out in it.
    </p>

    <!-- ================================================================== -->
    <!-- 8. What the Aporia Does Not Prove -->
    <!-- ================================================================== -->'''

new_after_asymmetry = '''
    <!-- ================================================================== -->
    <!-- 7. What the Aporia Does Not Prove -->
    <!-- ================================================================== -->'''

content = content.replace(old_second_edge, new_after_asymmetry)

# ============================================================
# 6. Renumber §8 → §7 (What the Aporia Does Not Prove)
# ============================================================
content = content.replace(
    '<h2 id="limits">8. What the Aporia Does Not Prove</h2>',
    '<h2 id="limits">7. What the Aporia Does Not Prove</h2>'
)

# ============================================================
# 7. Fix the "limits" bullet about volitional responses / second edge
# ============================================================
content = content.replace(
    '        <li>The aporia does not extend to volitional responses: for them the fourth condition is fulfilled <em>a fortiori</em> (p.318). Only the second, avowedly weaker edge reaches them.</li>\n',
    '        <li>The aporia does not extend to volitional responses: for them the fourth condition is fulfilled <em>a fortiori</em> (p.318), and sanction is not required.</li>\n'
)

# ============================================================
# 8. Renumber §9 → §8 (Anticipation of Defenses)
# ============================================================
content = content.replace(
    '<h2 id="defenses">9. Anticipation of Defenses</h2>',
    '<h2 id="defenses">8. Anticipation of Defenses</h2>'
)
content = content.replace(
    '<h3 id="defense-1">9.1. Defense One:',
    '<h3 id="defense-1">8.1. Defense One:'
)
content = content.replace(
    '<h3 id="defense-2">9.2. Defense Two:',
    '<h3 id="defense-2">8.2. Defense Two:'
)
content = content.replace(
    '<h3 id="defense-3">9.3. Defense Three:',
    '<h3 id="defense-3">8.3. Defense Three:'
)

# Also update the comment
content = content.replace(
    '<!-- 9. Anticipation of Defenses -->',
    '<!-- 8. Anticipation of Defenses -->'
)

# ============================================================
# 9. Update "three lines of defense" to match renumbering
# ============================================================
content = content.replace(
    'Now three lines of defense',
    'Now three lines of defense'
)  # no change needed here

# ============================================================
# Write output
# ============================================================
with open('/tmp/fixed_hildebrand.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done. Output length: {len(content)} chars, {content.count(chr(10))} lines")

# Verify key sections exist
for marker in [
    'Illustrative Example: The Paradox of Contrition',
    '3. The Six Principles',
    '4. The Aporia of the Heart',
    '5. Three Objections',
    '6. The Decisive Blow',
    '7. What the Aporia Does Not Prove',
    '8. Anticipation of Defenses',
    '8.1. Defense One',
    '8.2. Defense Two',
    '8.3. Defense Three',
]:
    if marker in content:
        print(f"  ✓ Found: {marker}")
    else:
        print(f"  ✗ MISSING: {marker}")

# Verify removed sections are gone
for marker in [
    'False Attack',
    'Second Edge',
    'Aporia of Locus',
]:
    if marker in content:
        print(f"  ✗ STILL PRESENT: {marker}")
    else:
        print(f"  ✓ Removed: {marker}")